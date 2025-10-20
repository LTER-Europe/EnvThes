# 🧩 eLTER-RI Controlled Vocabulary – Environmental Thesaurus (EnvThes)

[![FAIR RDF Generation](https://github.com/LTER-Europe/EnvThes/actions/workflows/sheet2rdf.yml/badge.svg?branch=main)](https://github.com/LTER-Europe/EnvThes/actions/workflows/sheet2rdf.yml)

The **Environmental Thesaurus (EnvThes)** is the controlled vocabulary of the [eLTER-RI](https://www.elter-ri.eu/) Research Infrastructure.  
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

EnvThes vocabulary is licensed under [**CC BY 4.0**](https://creativecommons.org/licenses/by/4.0/).

---

## 🧩 Configuring *sheet2rdf*

If you want to use **sheet2rdf** in your own work, follow these steps to configure it for your vocabulary repository:

1. Generate a [Google API key](https://developers.google.com/sheets/api/guides/authorizing#APIKey) with read-only access to Google Sheets.  
2. Create the following [**GitHub Secrets**](https://docs.github.com/en/actions/security-guides/encrypted-secrets):

| Secret | Explanation | Example configuration for *EnvThes* |
|--------|--------------|--------------------------------------|
| `FILE_NAME` | Base name used for the generated `.ttl`, `.xlsx`, and `.csv` files | `EnvThes` |
| `SHEET_ID` | Unique ID of the Google Sheet to be fetched | [1GJm6ojP8_Wlp6fJppqhNrrUK4fWv03ckTbVVnye494A](https://docs.google.com/spreadsheets/d/1GJm6ojP8_Wlp6fJppqhNrrUK4fWv03ckTbVVnye494A/edit?pli=1&gid=107934398#gid=107934398) |
| `GOOGLE_API_KEY` | Google API key with read access to the spreadsheet | `AIza...` |

The workflow will automatically:
- Fetch the content of the tab defined by `SHEET_TAB_NAME` (in this case `EnvThes`)  
- Convert it into `.xlsx`, `.csv`, and `.ttl` formats  
- Commit the generated files and logs to this repository  
- Create a new tagged release with extracted FAIR metadata and license information

---

## 🧭 Acknowledgements

This work builds on the efforts of the [eLTER-RI](https://elter-ri.eu/) communities, with support from multiple projects contributing to the development of interoperable and FAIR semantic resources for environmental research infrastructures.

---

## 💡 Related vocabularies

| Vocabulary | Description | Access |
|-------------|--------------|--------|
| **[SO – Standard Observations](https://github.com/LTER-Europe/SO)** | Controlled vocabulary describing eLTER Standard Observations (SOs) variables, methods, and protocols | [View in Skosmos](https://vocabs.lter-europe.net/so/en/) |
| **[CL – Controlled Lists](https://github.com/LTER-Europe/eLTER_CL)** | Standardised lists of values used across eLTER metadata systems | [View in Skosmos](https://vocabs.lter-europe.net/cl/en/) |
| **[EnvThes – Environmental Thesaurus](https://github.com/LTER-Europe/EnvThes)** | Common semantic framework for environmental parameters and concepts | [View in Skosmos](https://vocabs.lter-europe.net/envthes/en/) |
