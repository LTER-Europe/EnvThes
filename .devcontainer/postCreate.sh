#!/bin/bash
set -euxo pipefail

# Remove ready signal
rm -f /workspaces/.postcreate_done

# Set up the environment
eval "$(conda shell.bash hook)"
conda config --add channels conda-forge
conda config --set channel_priority strict
conda create -y -n sheet2rdf_dev python=3.8 pandas openpyxl requests rdflib shyaml
conda activate sheet2rdf_dev

# Download the vocabulary and convert it to ttl
curl -L https://github.com/sparna-git/xls2rdf/releases/download/2.1.1/xls2rdf-app-2.1.1-onejar.jar -o xls2rdf.jar
python src/sheet2xls.py
java -jar xls2rdf.jar convert -i $FILE_NAME.xlsx -o $FILE_NAME.ttl -l en
mv xls2rdf.log ./logs/
python src/update.py

# Clone the Skosmos source
if [ ! -d "skosmos-src" ]; then
  git clone --depth 1 https://github.com/NatLibFi/Skosmos.git skosmos-src
# If we rebuild the dev container, undo the changes we made to the config
else
  git -C skosmos-src restore -- dockerfiles/config/config-docker-compose.ttl
  rm -f skosmos-src/dockerfiles/config/config-docker-compose.ttl.bak
fi

# Compute baseHref from Codespace name
BASEHREF="https://${CODESPACE_NAME//_/-}-9090.app.github.dev/"

# Generate vocabulary block info
python src/generate_vocab_block.py ./$FILE_NAME.ttl > /tmp/vocab-block.ttl

# Write config for Skosmos
# Change the baseHref 
sed -i.bak \
  -e 's|^[[:space:]]*# *skosmos:baseHref "http://localhost/Skosmos/" ;|    skosmos:baseHref "'"${BASEHREF}"'" ;|' \
  skosmos-src/dockerfiles/config/config-docker-compose.ttl

# Delete default vocabulary blocks
sed -i.bak -e '/^:unesco /,/^ *\.$/d' -e '/^:stw /,/^ *\.$/d' skosmos-src/dockerfiles/config/config-docker-compose.ttl

# Append the generated vocabulary block info
cat /tmp/vocab-block.ttl >> skosmos-src/dockerfiles/config/config-docker-compose.ttl

# Sometimes Docker is not ready when we want to use it, so we want to make sure it is ready
ensure_docker() {
  if ! docker info >/dev/null 2>&1; then
    echo "[INFO] Starting Docker daemon…"
    sudo /usr/local/share/docker-init.sh || true
  fi
  for i in {1..90}; do
    if docker info >/dev/null 2>&1; then
      echo "[INFO] Docker is ready."
      return 0
    fi
    echo "[INFO] Waiting for Docker…"
    sleep 1
  done
  echo "[ERROR] Docker daemon did not become ready."
  ps -ef | grep -E '[d]ockerd' || true
  sudo tail -n 200 /var/log/dockerd.log 2>/dev/null || true
  exit 1
}

# Wait for Docker
ensure_docker

# Retry Docker-compose three times in case the daemon flaps
for a in 1 2 3; do
  if docker compose -f skosmos-src/docker-compose.yml up -d --build; then
    break
  fi
  echo "[WARN] docker compose failed (attempt $a), retrying in 3s…"
  sleep 3
  ensure_docker
done

# Wait until SPARQL endpoint is ready
for i in {1..60}; do
  if curl -sS -G 'http://localhost:9030/skosmos/sparql' --data-urlencode 'query=ASK{}' -H 'Accept: text/boolean' -o /dev/null; then break; fi
  sleep 1
done

# Load TTL into the graph
curl --retry 6 --retry-delay 2 --retry-connrefused -sSf -X PUT -H "Content-Type: text/turtle;charset=utf-8" --data-binary @$FILE_NAME.ttl "http://localhost:9030/skosmos/data?graph=http://example.org/graph/dev"

# Signal that post-create finished
touch /workspaces/.postcreate_done
