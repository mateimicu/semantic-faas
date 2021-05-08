#!/usr/bin/env python3
"""
Generate a turtle document with all the aws zones.
"""
import os
import itertools
import json

from rdflib import Graph, Literal
from rdflib.namespace import RDFS, RDF, URIRef
from wikidata.client import Client
WIKIDATA_ENTITY_PREFIX = 'http://www.wikidata.org/entity/'

"""
:Ohio rdf:type locn:Address ;
      locn:addressArea "Ohio" .
:us-east-2a rdf:type :datacenter .
locn:address :Ohio .

"""

def main():
    aws = json.loads(open("./aws_regions.json", "r").read())
    g = Graph()
    g.bind("locn", "http://www.w3.org/ns/locn#")
    g.bind("wd", "http://www.wikidata.org/entity/")
    g.bind("", "http://www.semantic-faas.com/ontology#")
    for region in aws:
        # create region
        region_node = URIRef("http://www.semantic-faas.com/ontology#"+region["name"].replace(" ", "_"))
        g.add([region_node, RDF.type, URIRef("http://www.w3.org/ns/locn#Address")])
        g.add([region_node, URIRef("http://www.w3.org/ns/locn#addressArea"), Literal(region["name"])])
        g.add([region_node, RDFS.label, Literal(region["name"])])
        g.add([region_node, RDFS.comment, Literal(region["full_name"])])

        for zone in region["zones"]:

            zone_node = URIRef("http://www.semantic-faas.com/ontology#"+zone)
            g.add([zone_node, RDF.type, URIRef("http://www.wikidata.org/entity/Q671224")])
            g.add([zone_node, RDFS.label, Literal(zone)])
            g.add([zone_node, URIRef("http://www.w3.org/ns/locn#addressArea"), region_node])

    g.serialize("aws.owl", format="turtle")


if __name__ == '__main__':
    main()


