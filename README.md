[![DOI](https://zenodo.org/badge/311036851.svg)](https://zenodo.org/badge/latestdoi/311036851) [![CI](https://github.com/niva83/sheet2rdf/workflows/Sheet2RDF/badge.svg)](https://github.com/fair-data-collective/excel2rdf-template/actions?query=workflow%3Aexcel2rdf)

# sheet2rdf

This repository hosts automatic workflow, executed by means of Github actions, and underlying shell and python scripts which:

- Converts Google Sheet to machine-actionable and FAIR RDF vocabulary
- Tests the converted vocabulary
- Commits conversion results and tests logs to this repository
- and deploy RDF vocabulary to OntoStack to be served to humans and machines

This workflow is an extension of [excel2rdf](https://github.com/fair-data-collective/excel2rdf-template).

# OntoStack

OntoStack is a set of orchestrated micro-services configured and interfaced such that they can intake vocabularies and resolve their terms and RDF properties upon requests either by humans or machines.

Some of OntoStack micro-services are:

- [Jena Fuseki](https://jena.apache.org/documentation/fuseki2/) a graph database
- [SKOSMOS](http://www.skosmos.org/) a web-based SKOS browser acting as a front-end for the vocabularies persisted by the graph database
- [Træfik](https://doc.traefik.io/traefik/) an edge router responsible for proper serving of URL requests

Currently two instances of OntoStack run on:

- DTU Wind Energy web server: http://data.windenergy.dtu.dk/ontologies
- DeiC VM: http://ontology.deic.dk/

# Configuring sheet2rdf

In case you want to use **sheet2rdf** in your own work you need to:

1. Follow [gsheets](https://pypi.org/project/gsheets/) Quickstart and generate client_secrets.json and storage.json

2. Create following [Github secrets](https://docs.github.com/en/free-pro-team@latest/actions/reference/encrypted-secrets):
   - **DB_USER**: user name of Jena Fuseki user account that has privilages to PUT RDF vocabulary to the database
   - **DB_PASS**: password of for the above account
   - **FILE_NAME**: name that will be used when converting of Google sheet to files such as RDF and CSB down in the workflow.
   - **GRAPH**: graph in the database to which the above RDF vocabulary should be deployed.
   - **SHEET_ID**: unique ID of the sheet that will be fetch from Google drive.
   - **SPARQL_ENDPOINT**: endpoint to which RDF vocabulary is PUT.
   - **STORAGE**: content of storage.json
   - **CLIENT**: content of client.json

# License

This work is licensed under [Apache 2.0 License](https://github.com/niva83/sheet2rdf/blob/main/License.md).
