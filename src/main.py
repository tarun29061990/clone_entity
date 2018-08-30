import json
import sys

from graph import Graph

class Main():
    def main(self, input_file_path, entity_id_to_be_cloned):


        input_data = ""
        with open(input_file_path, mode="r") as data:
            for line in data:
                input_data += line

        input_data = json.loads(input_data)

        # creating graph of all the entities
        entity_graph = Graph()

        entity_graph = self.create_entity_graph(entity_graph, input_data)

        if entity_id_to_be_cloned:
            cloned_entity = entity_graph.clone_entity(entity_id_to_be_cloned, {})

            # entities that link to  initial entity i.e. source_entity must now also link to the clone of the source_entity
            source_entity_id_parents = entity_graph.get_entity_parents(entity_id_to_be_cloned)
            for source_entity_id_parent in source_entity_id_parents:
                entity_graph.add_edge(source_entity_id_parent.entity_id, cloned_entity.entity_id)

        # printing to std output after cloning the entity
        graph_json = entity_graph.print_graph()
        return graph_json

    def create_entity_graph(self, entity_graph, data):
        # adding entites as vertices in a graph
        if len(data["entities"]):
            for entity in data["entities"]:
                entity_graph.add_vertex(entity)

        # adding links as edges in entity graph
        if len(data["links"]):
            for link in data["links"]:
                entity_graph.add_edge(link["from"], link["to"])

        return entity_graph


if len(sys.argv) > 1:
    input_file_path = sys.argv[1]
    entity_id_to_be_cloned = int(sys.argv[2])
    Main().main(input_file_path, entity_id_to_be_cloned)
