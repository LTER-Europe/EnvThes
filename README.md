# EnvThes
EnvThes (Environmental Thesaurus) is the controlled vocabulary of the LTER-Europe community. It is coordinated by Umweltbundesamt GmbH, Austria. Here you can find the repository of the SKOS vocabulary. If you want to contribute to EnvThes with suggestions of new terms you have to create a gitHub account first. For any addition of new terms or modification of existing terms please add a new issue. For more information on how to do this please consult the Wiki page.

Versioning management: 
For EnvThes two types of versioning are considered.
Big changes in structure are stored separately. Older versions are put in the related directory. 
The current version is stored as EnvThes.ttl under this directory. EnvThes versions with smaller changes are overwritten in this repository. For the EnvThes management the sheet2rdf workflow as described below is used. 

EnvThes is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).


You can view EnvThes here: http://vocabs.lter-europe.net/EnvThes/

# sheet2rdf

This repository hosts automatic workflow, executed by means of Github actions, and underlying shell and python scripts which:

- Fetches Google Sheet from Google Drive and stores is as `xlsx` and `csv` files
- Converts fetched sheet to machine-actionable and FAIR RDF vocabulary using [xls2rdf](https://github.com/sparna-git/xls2rdf)
- Tests the resulting RDF vocabulary using [qSKOS](https://github.com/cmader/qSKOS/)
- Commits conversion results and tests logs to this repository
- and deploy RDF vocabulary to OntoStack to be served to humans and machines

This workflow is an extension of [excel2rdf](https://github.com/fair-data-collective/excel2rdf-template).

This work is licensed under [Apache 2.0 License](https://github.com/niva83/sheet2rdf/blob/main/License.md).

Nikola Vasiljevic. (2021, January 11). sheet2rdf: First release (Version v0.1). Zenodo. http://doi.org/10.5281/zenodo.4432136
