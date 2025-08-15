import os
import requests

FILE_NAME = os.environ['FILE_NAME']

RENDERING_UPDATE = """@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix schema: <http://schema.org/>.
@prefix iop:   <https://w3id.org/iadopt/ont/> .
@prefix puv: <https://w3id.org/env/puv#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .

iop:constrains  a     owl:ObjectProperty ;
        rdfs:comment  "A Constraint constrains an Entity having a role in the Variable description." ;
        rdfs:domain   iop:Constraint ;
        rdfs:label    "constrains" ;
        rdfs:range    iop:Entity .

iop:hasConstraint  a  owl:ObjectProperty ;
        rdfs:comment  "A Variable has a Constraint, that confines an Entity involved in the observation." ;
        rdfs:domain   iop:Variable ;
        rdfs:label    "hasConstraint" ;
        rdfs:range    iop:Constraint .

iop:hasContextObject  a  owl:ObjectProperty ;
        rdfs:comment  "A Variable has an Entity that provides additional background information regarding the ObjectOfInterest." ;
        rdfs:domain   iop:Variable ;
        rdfs:label    "hasContextObject" ;
        rdfs:range    iop:Entity .

iop:hasMatrix  a            owl:ObjectProperty ;
        rdfs:comment        "A Variable might have an Entity in which the ObjectOfInterest is contained." ;
        rdfs:domain         iop:Variable ;
        rdfs:label          "hasMatrix" ;
        rdfs:range          iop:Entity ;
        rdfs:subPropertyOf  iop:hasContextObject .

iop:hasObjectOfInterest
        a             owl:ObjectProperty ;
        rdfs:comment  "A Variable has an Entity whose Property is observed." ;
        rdfs:domain   iop:Variable ;
        rdfs:label    "hasObjectOfInterest" ;
        rdfs:range    iop:Entity .

iop:hasProperty  a    owl:ObjectProperty ;
        rdfs:comment  "A Variable has a Property that characterizes an Entity." ;
        rdfs:domain   iop:Variable ;
        rdfs:label    "hasProperty" ;
        rdfs:range    iop:Property .

puv:uom
  a owl:ObjectProperty ;
  rdfs:comment "scale or unit of measurement" ;
  rdfs:label "unit-of-measurement " ;
  rdfs:range puv:UnitOfMeasurement .

puv:statistic
  a owl:ObjectProperty ;
  rdfs:comment "statistical treatment" ;
  rdfs:domain puv:Parameter ;
  rdfs:label "statistic " ;
  rdfs:range puv:ParameterStatistic .

puv:method
  a owl:ObjectProperty ;
  rdfs:comment "method used to measure the value" ;
  rdfs:label "method" ;
  rdfs:range puv:Method .

sosa:madeBySensor 
  a owl:ObjectProperty ;
  rdfs:label "made by sensor"@en ;
  skos:definition "Relation between an Observation and the Sensor which made the Observation."@en ;
  rdfs:comment "Relation between an Observation and the Sensor which made the Observation."@en ;
  schema:domainIncludes sosa:Observation ;
  schema:rangeIncludes sosa:Sensor ;
  owl:inverseOf sosa:madeObservation ;
  rdfs:isDefinedBy sosa: .
"""

vocab_file = open(f"./{FILE_NAME}.ttl", "r")
vocab = vocab_file.read()
vocab_file.close()

vocab = vocab.replace("@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .", RENDERING_UPDATE)

vocab_file = open(f"./{FILE_NAME}.ttl", "w")
vocab_file.write(vocab)
vocab_file.close()
