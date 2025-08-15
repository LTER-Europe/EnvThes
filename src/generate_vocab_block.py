#!/usr/bin/env python3
import argparse
from pathlib import Path
from rdflib import Graph, RDF, RDFS, URIRef, Literal
from rdflib.namespace import SKOS, DCTERMS

LABEL_PROPS = [SKOS.prefLabel, SKOS.altLabel, SKOS.hiddenLabel, RDFS.label]

def detect_title(graph):
    for s in graph.subjects(RDF.type, SKOS.ConceptScheme):
        for p in (DCTERMS.title, RDFS.label):
            o = graph.value(s, p)
            if isinstance(o, Literal):
                return str(o), o.language
    for p in (DCTERMS.title, RDFS.label):
        for o in graph.objects(None, p):
            if isinstance(o, Literal):
                return str(o), o.language
    return None, None

def detect_languages(graph):
    langs = set()
    for p in LABEL_PROPS:
        for o in graph.objects(None, p):
            if isinstance(o, Literal) and o.language:
                langs.add(o.language.lower())
    return sorted(langs)

def longest_common_prefix(uris):
    if not uris:
        return None
    s1 = min(uris)
    s2 = max(uris)
    i = 0
    for i, c in enumerate(s1):
        if i >= len(s2) or c != s2[i]:
            break
    prefix = s1[:i]
    cut = max(prefix.rfind('/'), prefix.rfind('#'))
    if cut > 0:
        prefix = prefix[:cut+1]
    return prefix

def detect_uri_space(graph, sample_limit=5000):
    uris = []
    for i, s in enumerate(graph.subjects(RDF.type, SKOS.Concept)):
        if isinstance(s, URIRef):
            uris.append(str(s))
        if i >= sample_limit:
            break
    return longest_common_prefix(uris)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ttl", help="Path to vocabulary TTL file")
    args = ap.parse_args()

    g = Graph()
    g.parse(args.ttl, format="turtle")

    title_auto, _ = detect_title(g)
    title = title_auto or Path(args.ttl).stem

    short = Path(args.ttl).stem.lower().replace(" ", "-")

    langs_auto = detect_languages(g)
    langs = [l.lower() for l in (langs_auto or ["en"])]
    default_lang = "en" if "en" in langs else (langs[0] if langs else "en")
    langs_list = ", ".join(f"\"{l}\"" for l in langs)

    uri_space = detect_uri_space(g) or "http://example.org/concept/"
    
    print(f"""
:{short} a skosmos:Vocabulary, void:Dataset ;
  dc:title "{title}"@{default_lang} ;
  skosmos:shortName "{short}" ;
  skosmos:language {langs_list} ;
  skosmos:defaultLanguage "{default_lang}" ;
  void:uriSpace "{uri_space}" ;
  void:sparqlEndpoint <http://fuseki:3030/skosmos/sparql> ;
  skosmos:sparqlGraph <http://example.org/graph/dev> ;
  skosmos:showTopConcepts true ;
  skosmos:fullAlphabeticalIndex true .
""".strip())

if __name__ == "__main__":
    main()
