#!/usr/bin/env python
"""
Utility to parse a .owl document and add labels to all WikiData elements.
"""
import os
import itertools

from rdflib import Graph, Literal
from rdflib.namespace import RDFS
from wikidata.client import Client
WIKIDATA_ENTITY_PREFIX = 'http://www.wikidata.org/entity/'

def get_label(elem):
    client = Client()
    entity = client.get(elem.rsplit('/', 1)[-1], load=True)
    return Literal(entity.label)


def main():
    ontology_file = "faas.owl"
    ontology_file_output = "faas.owl"

    g = Graph()
    g.parse(ontology_file, format="n3")

    # get all wikidata elements
    wikidata_elements = []

    for elem in itertools.chain(g.subjects(), g.predicates(), g.objects()):
        if elem.startswith(WIKIDATA_ENTITY_PREFIX):
            wikidata_elements.append(elem)


    print(wikidata_elements)
    # if the label is missing fetch it and add it to our items
    for wd in wikidata_elements:
        if g.label(wd, default=None) is None:
            label = get_label(wd)
            g.add([wd, RDFS.label, label])
    g.serialize(ontology_file_output, format="turtle")

if __name__ == '__main__':
    main()
