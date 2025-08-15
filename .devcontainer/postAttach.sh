#!/usr/bin/env bash
set -euo pipefail

if [[ -f /workspaces/.postcreate_done ]]; then
  BASE="https://${CODESPACE_NAME//_/-}"
  echo
  echo "Setup complete"
  echo "Skosmos: ${BASE}-9090.app.github.dev/"
  echo
else
  echo
  echo "Setup has not finished successfully."
  echo "To check the logs, press F1 and run Codespaces: View creation log
  echo "To rebuild the Codespace container, press F1 and run Codespaces: Rebuild Container
  echo
fi
