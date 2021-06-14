#!/usr/bin/env python3
import pathlib
import sys
import argparse
def get_args(args):
    parser = argparse.ArgumentParser("test_sparql")
    parser.add_argument(
        "--ontology", help="Path to ontology", default="faas.owl")
    parser.add_argument(
        "--sparql-dir", help="Directory with spraql queryx's",
        default="./sparql")
    parser.add_argument(
        "--sparql-regex-query", help="Regex to filter desired files from --sparql-dir",
        default="*.sparql")
    parser.add_argument("--inferences", help="RDF triples with interventions",
                        default=None)

    return parser.parse_args(args)


from rdflib import Graph


def main():
    args = get_args(sys.argv[1:])
    query_list = sorted(pathlib.Path(args.sparql_dir).rglob(args.sparql_regex_query))
    graph = Graph()
    graph.parse(args.ontology, format="n3")
    if args.inferences:
        graph.parse(args.inferences)

    for query in query_list:
        results = graph.query(open(query).read())
        print(query, end="\n"*2)
        for row in results:
            print(row)
        print(end="\n"*2)
        print(f"Suitable results: {len(results)}")
        print("-"*80, end="\n"*2)


if __name__  == '__main__':
    main()
