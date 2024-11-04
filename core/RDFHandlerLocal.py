import shutil
import subprocess
from SPARQLWrapper import SPARQLWrapper, DIGEST, POST, GET, TURTLE, CSV, JSON, XML
from rdflib import Graph

class RDFHandler:
    def __init__(
        self,
        _user,
        _password,
        kg_files_directory,
        sparql_endpoint,
    ):
        self._user = _user
        self._password = _password
        self.kg_files_directory = kg_files_directory
        self.sparql_endpoint = sparql_endpoint

    def execute_isql_command(self, sql_command):
        command = f"isql -S 1111 -U {self._user} -P {self._password} {sql_command}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print(result.stdout)
        return result

    def reset_db(self):
        sql_command = f"""exec="RDF_GLOBAL_RESET ();\""""
        return self.execute_isql_command(sql_command)

    def upload_rdf_file(self, rdf_file_path, container_rdf_folder, graph_iri):
        new_rdf_file_path = f"{self.kg_files_directory}/{rdf_file_path.split('/')[-1]}"
        shutil.move(rdf_file_path, new_rdf_file_path)

        sql_command = f"""exec="DELETE FROM DB.DBA.LOAD_LIST; 
                            ld_dir('{container_rdf_folder}',
                            '{rdf_file_path.split('/')[-1]}',
                            '{graph_iri}');
                            DB.DBA.rdf_loader_run();
                            checkpoint;\""""
        return self.execute_isql_command(sql_command)

    def delete_graph_from_file(self, rdf_file_path):
        new_rdf_file_path = f"{self.kg_files_directory}/{rdf_file_path.split('/')[-1]}"
        shutil.move(rdf_file_path, new_rdf_file_path)
        
        sql_command = f"""exec="
                            ld_dir('/opt/virtuoso-opensource/database/kg_files',
                            '{rdf_file_path.split('/')[-1]}',
                            'http://example.com/data_2');
                            DB.DBA.rdf_loader_run();
                            log_enable(3,1);
                            Delete from rdf_quad a 
                            where exists (select * from rdf_quad b
                            where a.s = b.s and a.p = b.p and a.o = b.o 
                            and b.g = iri_to_id('http://example.com/data_2')
                            and a.g = iri_to_id('http://example.com/data_1'));\""""
        return self.execute_isql_command(sql_command)

    def delete_triple(self, sparql_endpoint, subject, predicate, object, graph_iri):
        """
        Deletes a triple from the graph.
        """
        sparql = SPARQLWrapper(sparql_endpoint)
        sparql.setHTTPAuth(DIGEST)
        sparql.setCredentials(self._user, self._password)
        sparql.setMethod(POST)
        # query = "DELETE { ?s ?p ?o } WHERE {GRAPH <http://example.com/data_1> {?s ?p ?o}}".format(subject=subject, predicate=predicate, object=object, graph_iri=graph_iri)
        # query = f"DELETE {{ ?s ?p ?o }} WHERE {{GRAPH <{graph_iri}> {{{subject} {predicate} {object}}}}}"
        query = f"WITH <{graph_iri}> DELETE {{ {subject._value} {predicate._value} {object._value} }}"
        sparql.setQuery(query)
        # sparql.setReturnFormat(TURTLE)

        g = sparql.query()

        for row in g:
            print(row)

        return g

    def query(self, sparql_endpoint, query):
        sparql = SPARQLWrapper(sparql_endpoint)
        sparql.setHTTPAuth(DIGEST)
        sparql.setCredentials(self._user, self._password)
        sparql.setQuery(query)
        # sparql.setReturnFormat(TURTLE)

        g = sparql.query()._convertRDF()

        # self.print_sample_triples(g)
        return g

    def print_sample_triples(self, graph, num_triples=10):
        print(f"Printing {num_triples} sample triples:")
        for i, (s, p, o) in enumerate(graph):
            if i >= num_triples:
                break
            print(f"{s} {p} {o}")
