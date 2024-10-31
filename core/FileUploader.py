import os
import sys
import rdflib
from rdflib import Graph, URIRef, Literal, BNode
from rdflib.namespace import RDF, XSD, FOAF
from RDFHandler import RDFHandler 

def main():
    rdfHandler = RDFHandler(
        container_name="virtuoso",
        _user="dba",
        _password="my_strong_password",
        kg_files_directory="./core/data/virtuoso_data/kg_files",
        sparql_endpoint="http://localhost:8890/sparql",
    )
    
    # new_triplets_graph = rdflib.Graph(identifier="http://example.com/data_1")
    # new_triplets_graph.bind("schema", URIRef("https://schema.org/"))
    rdfHandler.load_graph(rdf_file_path="./core/data/datasets_data/dataset_333_croissant_OpenML.jsonld")
    print("VIRTUOSO LOADED")
    check_graph_triplets(rdfHandler)
    

def check_graph_triplets(rdfHandler):
    
    result_graph = rdfHandler.query(
        "http://virtuoso:8890/sparql",
        """CONSTRUCT { ?s ?p ?o } WHERE {GRAPH <http://example.com/data_1> {?s ?p ?o}}""",
    )
    
    print("VIRTUOSO TRIPlETS\n")
    for i, (s, p, o) in enumerate(result_graph):
        print(f"{i}: {s} {p} {o}")

    result_count = result_graph.query(
        """SELECT (COUNT(DISTINCT ?s) AS ?count) WHERE{?s ?p ?o}"""
    )
    
    for triple in result_count:
        print("VIRTUOSO MODEL COUNT\n", triple.asdict()["count"]._value)

main()