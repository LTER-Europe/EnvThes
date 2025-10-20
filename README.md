# 🧩 eLTER-RI Controlled Vocabulary – Environmental Thesaurus (EnvThes)

[![FAIR RDF Generation](https://github.com/LTER-Europe/EnvThes/actions/workflows/sheet2rdf.yml/badge.svg?branch=main)](https://github.com/LTER-Europe/EnvThes/actions/workflows/sheet2rdf.yml)

The **Environmental Thesaurus (EnvThes)** is the controlled vocabulary of the [LTER-Europe](https://www.lter-europe.net/) community.  
It is coordinated by **Umweltbundesamt GmbH (Austria)** and provides a common semantic framework for describing environmental data and observations across European Long-Term Ecosystem Research (eLTER) sites.  

EnvThes supports **metadata interoperability** and **semantic harmonisation** by providing a shared vocabulary for environmental variables, parameters, and related concepts.  
It is a key component for ensuring **FAIR, standardised and discoverable environmental information** within the eLTER Information System.

📘 **Vocabulary access:** [https://vocabs.lter-europe.net/EnvThes/](https://vocabs.lter-europe.net/EnvThes/)

---

## ⚙️ Automated FAIR Workflow — *sheet2rdf*

This repository is automatically updated through the [**sheet2rdf**](https://github.com/nikokaoja/sheet2rdf) workflow, which ensures that the vocabulary remains FAIR and synchronised with its authoritative Google Sheet source.

The workflow automatically:

1. Fetches the Google Sheet source as `.xlsx` and `.csv` files  
2. Converts the sheet to RDF (Turtle) using [**xls2rdf**](https://github.com/sparna-git/xls2rdf)  
3. Commits the generated `.ttl`, `.xlsx`, and log files to this repository  
4. Publishes the resulting RDF to the [**Skosmos vocabulary server**](https://vocabs.lter-europe.net)

This workflow extends [**excel2rdf**](https://github.com/fair-data-collective/excel2rdf-template) and is licensed under the [Apache 2.0 License](https://github.com/nikokaoja/sheet2rdf/blob/main/License.md).

🧾 **Workflow provenance:**  
> This file has been modified from its originally licensed version by *WillOnGit* – see [README.md](https://github.com/LTER-Europe/EnvThes) at repository root for license information.

📚 **Citation:**  
> Nikola Vasiljevic. (2021, January 11). *sheet2rdf: First release* (Version v0.1). Zenodo. [https://doi.org/10.5281/zenodo.4432136](https://doi.org/10.5281/zenodo.4432136)

---

## 🧠 Repository contents

| File | Description |
|------|--------------|
| [EnvThes.ttl](https://github.com/LTER-Europe/EnvThes/blob/main/EnvThes.ttl) | RDF (Turtle) representation of the eLTER Environmental Thesaurus |
| [EnvThes.xlsx](https://github.com/LTER-Europe/EnvThes/blob/main/EnvThes.xlsx) | Source spreadsheet fetched from Google Sheets |
| [EnvThes.csv](https://github.com/LTER-Europe/EnvThes/blob/main/EnvThes.csv) | CSV export of the vocabulary |
| [logs/](https://github.com/LTER-Europe/EnvThes/tree/main/logs) | Conversion logs produced during RDF generation |
| [.github/workflows/sheet2rdf.yml](https://github.com/LTER-Europe/EnvThes/blob/main/.github/workflows/sheet2rdf.yml) | GitHub Action workflow automating the FAIR publication process |

---

## 💬 Contributing

If you wish to propose new terms or suggest modifications to existing ones:

- Please create a [GitHub account](https://github.com/signup)  
- Open a new [issue](https://github.com/LTER-Europe/EnvThes/issues) describing your proposal  
- Consult the project [Wiki page](https://github.com/LTER-Europe/EnvThes/wiki) for detailed instructions

EnvThes is licensed under [**CC BY 4.0**](https://creativecommons.org/licenses/by/4.0/).
