#!/usr/bin/env python3
import pathlib


from rdflib import Graph

QUERY = pathlib.Path("./sparql").rglob("*.sparql")

def main():
    ontology_file = "faas.owl"
    graph = Graph()
    graph.parse(ontology_file, format="n3")

    for query in QUERY:
        results = graph.query(open(query).read())
        print(query, end="\n"*2)
        for row in results:
            print(row)
        print(end="\n"*2)
        print(f"Suitable results: {len(results)}")
        print("-"*80, end="\n"*2)


if __name__  == '__main__':
    main()
