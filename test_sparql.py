#!/usr/bin/env python
from rdflib import Graph

QUERY = [
    'sparql/query_1.sparql',
    'sparql/query_2.sparql',
    'sparql/query_3.sparql',
    'sparql/query_4.sparql',
]

def main():
    ontology_file = "diz.owl"
    graph = Graph()
    graph.parse(ontology_file, format="n3")

    for query in QUERY:
        results = graph.query(open(query).read())
        print(query)
        print()
        for row in results:
            print(row)
        print()
        print()
        print()


if __name__  == '__main__':
    main()

