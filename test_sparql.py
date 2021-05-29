#!/usr/bin/env python
from rdflib import Graph

QUERY_1 = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX faas: <http://www.semantic-faas.com/ontology#>
SELECT  DISTINCT ?subject
WHERE {
  ?subject rdf:type owl:NamedIndividual .
  ?subject rdf:type faas:FaaSExecutionEnvironment .
}
"""

QUERY_2 = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX faas: <http://www.semantic-faas.com/ontology#>
SELECT  DISTINCT ?subject
WHERE {
  ?subject rdf:type owl:NamedIndividual .
  ?subject rdf:type faas:FaaSExecutionEnvironment .
  ?subject faas:datacenter ?datacenter .
}
GROUP BY ?subject
HAVING (count(distinct ?datacenter) >= 2)
"""


QUERY_3="""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX locn: <http://www.w3.org/ns/locn#>

PREFIX faas: <http://www.semantic-faas.com/ontology#>
SELECT  DISTINCT ?subject
WHERE {
  VALUES ?targetApplication { faas:CovidTracker }

  #### Filter for Geo Restrictions
  ?targetApplication faas:requirements ?geoRequirement .
  ?geoRequirement rdf:type faas:GeographicalRequirement .
  ?geoRequirement wdt:P361 ?desiredLocation .

  ?subject rdf:type owl:NamedIndividual .
  ?subject rdf:type faas:FaaSExecutionEnvironment .
  ?subject faas:datacenter ?datacenter .

  # at least one datacenter respects the geo restriction
  ?datacenter locn:addressArea ?addressArea .
  # P361 = part of
  ?addressArea wdt:P361 ?desiredLocation .

  #### Filter for ExecutionTime Restrictions

  ?targetApplication faas:requirements ?executionTIme .
  ?executionTIme rdf:type faas:ExecutionTimeRequirement .
  ?executionTIme faas:maxTimeAllowed ?maxTimeAllowed .

  ?subject faas:maxTimeAllowed ?SubjectMaxTimeAllowed .

  FILTER (xsd:integer(?SubjectMaxTimeAllowed) >= xsd:integer(?maxTimeAllowed))
}
"""

QUERY_4="""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX locn: <http://www.w3.org/ns/locn#>

PREFIX faas: <http://www.semantic-faas.com/ontology#>
SELECT  DISTINCT ?subject
WHERE {
  VALUES ?targetApplication { faas:EchoServer }

  ?subject rdf:type owl:NamedIndividual .
  ?subject rdf:type faas:FaaSExecutionEnvironment .

  #### Filter for ExecutionTime Restrictions
  ?targetApplication faas:requirements ?executionTIme .
  ?executionTIme rdf:type faas:ExecutionTimeRequirement .
  ?executionTIme faas:maxTimeAllowed ?maxTimeAllowed .

  ?subject faas:maxTimeAllowed ?SubjectMaxTimeAllowed .

  FILTER (xsd:integer(?SubjectMaxTimeAllowed) >= xsd:integer(?maxTimeAllowed))

  #### Filter for concurency
  ?targetApplication faas:requirements ?ConcurrencyRequirement .
  ?ConcurrencyRequirement rdf:type faas:ConcurrencyRequirement .
  ?ConcurrencyRequirement faas:minConcurrency ?minConcurrency .

  ?subject faas:maxConcurrency ?SubjectMaxConcurency .
  FILTER (xsd:integer(?SubjectMaxTimeAllowed) >= xsd:integer(?minConcurrency))

  #### Filter for CPU
  ?targetApplication faas:requirements ?CPURequirement .
  ?CPURequirement rdf:type faas:CPURequirement .
  ?CPURequirement faas:cpuArch ?cpuArch .

  ?subject faas:cpuArch ?cpuArch .

  #### Filter for CPU
  ?targetApplication faas:requirements ?MemoryRequirement .
  ?MemoryRequirement rdf:type faas:MemoryRequirement .
  ?MemoryRequirement faas:maxAllowedRAM ?maxAllowedRAM .

  ?subject faas:maxRAM ?SubjectMaxRAM .
  FILTER (xsd:integer(?SubjectMaxRAM) >= xsd:integer(?maxAllowedRAM))
}
"""


def main():
    ontology_file = "diz.owl"
    graph = Graph()
    graph.parse(ontology_file, format="n3")

    for query in [QUERY_1, QUERY_2, QUERY_3, QUERY_4]:
        results = graph.query(query)
        print(query)
        print()
        for row in results:
            print(row)
        print()
        print()
        print()


if __name__  == '__main__':
    main()

