import os
import sys
import rdflib
from rdflib import Graph, URIRef, Literal, BNode
from rdflib.namespace import RDF, XSD, FOAF
from RDFHandlerDocker import RDFHandler as RDFHandlerDocker
from RDFHandlerLocal import RDFHandler as RDFHandlerLocal

def main():
    test_docker_virtuoso()
    
def test_docker_virtuoso():
    rdfHandler = RDFHandlerDocker(
        container_name="virtuoso",
        _user="dba",
        _password="my_strong_password",
        kg_files_directory="./core/data/virtuoso_data/kg_files",
        sparql_endpoint="http://virtuoso:8890/sparql",
    )
    
    rdfHandler.reset_db()
    
    rdfHandler.upload_rdf_file(
                          
                          rdf_file_path="./core/data/datasets_data/dataset_333_croissant_OpenML.jsonld",
                          container_rdf_folder="/opt/virtuoso-opensource/database/kg_files",
                          graph_iri="http://example.com/data_1"
                          
                        )
    
    print("VIRTUOSO LOADED")
    
    endpoint = "http://virtuoso:8890/sparql"
    graph_iri = "http://example.com/data_1"
    
    check_graph_triplets(rdfHandler,endpoint,graph_iri)

def test_local_virtuoso():
    rdfHandler = RDFHandlerLocal(
        _user="dba",
        _password="my_strong_password",
        kg_files_directory="./core/data/virtuoso_data/kg_files",
        sparql_endpoint="http://localhost:8890/sparql",
    )
    
    rdfHandler.reset_db()
    
    rdfHandler.upload_rdf_file(
                          
                          rdf_file_path="./core/data/datasets_data/dataset_333_croissant_OpenML.jsonld",
                          container_rdf_folder="/opt/virtuoso-opensource/database/kg_files",
                          graph_iri="http://example.com/data_1"
                          
                        )
    
    print("VIRTUOSO LOADED")
    
    endpoint = "http://localhost:8890/sparql"
    
    check_graph_triplets(rdfHandler,endpoint)
    

def check_graph_triplets(rdfHandler,endpoint,graph_iri):
    
    result_graph = rdfHandler.query(
        endpoint,
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