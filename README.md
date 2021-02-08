[![DOI](https://zenodo.org/badge/327900313.svg)](https://zenodo.org/badge/latestdoi/327900313)
[![CI](https://github.com/niva83/sheet2rdf/workflows/Sheet2RDF/badge.svg)](https://github.com/niva83/sheet2rdf/actions?query=workflow%3ASheet2RDF)

# sheet2rdf

This repository hosts automatic workflow, executed by means of Github actions, and underlying shell and python scripts which:

- Fetches Google Sheet from Google Drive and stores is at `xlsx` and `csv` files
- Converts fetched sheet to machine-actionable and FAIR RDF vocabulary using [xls2rdf](https://github.com/sparna-git/xls2rdf)
- Tests the resulting RDF vocabulary using [qSKOS](https://github.com/cmader/qSKOS/)
- Commits conversion results and tests logs to this repository
- and deploy RDF vocabulary to OntoStack to be served to humans and machines

This workflow is an extension of [excel2rdf](https://github.com/fair-data-collective/excel2rdf-template).

# OntoStack

OntoStack is a set of orchestrated micro-services configured and interfaced such that they can intake vocabularies and resolve their terms and RDF properties upon requests either by humans or machines.

Some of OntoStack micro-services are:

- [Jena Fuseki](https://jena.apache.org/documentation/fuseki2/) a graph database
- [SKOSMOS](http://www.skosmos.org/) a web-based SKOS browser acting as a front-end for the vocabularies persisted by the graph database
- [Træfik](https://doc.traefik.io/traefik/) an edge router responsible for proper serving of URL requests

Currently three instances of OntoStack are available:

- Departamental instance of [DTU Wind Energy](https://www.vindenergi.dtu.dk/english/): http://data.windenergy.dtu.dk/ontologies
- National (Danish) instance run by [DeiC](https://deic.dk/): http://ontology.deic.dk/
- International instance run by [FAIR Data Collective](http://fairdatacollective.org/): http://vocab.fairdatacollective.org

# Configuring sheet2rdf

In case you want to use **sheet2rdf** in your own work you need to:

1. Follow [gsheets](https://pypi.org/project/gsheets/) Quickstart and generate client_secrets.json and storage.json

2. Create following [Github secrets](https://docs.github.com/en/free-pro-team@latest/actions/reference/encrypted-secrets):
   - **DB_USER**: user name of Jena Fuseki user account that has privilages to PUT RDF vocabulary to the database
   - **DB_PASS**: password of for the above account
   - **FILE_NAME**: file name that will be used when converting Google sheet to `.ttl` (RDF), `.xlsx`, and `.csv` files.
   - **GRAPH**: graph in the database under which the above RDF vocabulary should be stored.
   - **SHEET_ID**: unique ID of the sheet that will be fetched from Google drive.
   - **SPARQL_ENDPOINT**: endpoint to which RDF vocabulary is PUT.
   - **STORAGE**: content of storage.json
   - **CLIENT**: content of client.json

# License

This work is licensed under [Apache 2.0 License](https://github.com/niva83/sheet2rdf/blob/main/License.md)


# Citation

In case you are using this workflow the author kindly requests you to cite this repository in your publications such as:
> Nikola Vasiljevic. (2021, January 11). sheet2rdf: First release (Version v0.1). Zenodo. http://doi.org/10.5281/zenodo.4432136

For any other citation format visit http://doi.org/10.5281/zenodo.4432136
