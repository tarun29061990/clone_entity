
# vertex class
# constructor takes node object as a parameter
# node -
#       entity_id - ID of an entity (mandatory)
#       name - name of an entity (mandatory)
#       description - description of an entity (optional)
class Vertex():
    def __init__(self, node):
        self.entity_id = node["entity_id"] if "entity_id" in node else ""
        self.name = node["name"] if "name" in node else ""
        if "description" in node:
            self.description = node["description"]
        self.neighbours = set()

    def get_id(self):
        return self.entity_id

    def add_neighbour(self, neighbour):
        if neighbour not in self.neighbours:
            self.neighbours.add(neighbour)

    def get_connections(self):
        return self.neighbours

    def get_parent(self, vertices):
        for v in vertices:
            entity = vertices[v]
            for neighbour in entity.neighbours:
                if neighbour.entity_id == self.entity_id:
                    return entity

# graph class
# Keeps track of no of vertices and all the vertices in a vertex object
class Graph():
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def add_vertex(self, node):
        if "entity_id" in node and node["entity_id"] not in self.vertices:
            new_vertex = Vertex(node)
            self.vertices[node["entity_id"]] = new_vertex
            self.num_vertices += 1
            return new_vertex

    def add_edge(self, from_id, to_id):

        if from_id not in self.vertices:
            self.add_vertex({"entity_id": from_id, "name": ''})
        if to_id not in self.vertices:
            self.add_vertex({"entity_id": to_id, "name": ''})

        self.vertices[from_id].add_neighbour(self.vertices[to_id])

    def get_vertices(self):
        return self.vertices.keys()

    def get_entity_parents(self, entity_id):
        parents = []
        for vertex in self.vertices:
            entity = self.vertices[vertex]
            for neighbour in entity.neighbours:
                if neighbour.entity_id == entity_id:
                    parents.append(entity)
        return parents

    def is_neighbour(self, entity_id_1, entity_id_2):
        entity_1 = self.vertices[entity_id_1]
        entity_2 = self.vertices[entity_id_2]

        if entity_2 in entity_1.get_connections():
            return True

        return False

    # This functions clones an entity and all the related entities to the cloned entities
    # Params - source_entity_id - ID that needs to be cloned
    #          entity_map - Map to store mappings of cloned entities
    def clone_entity(self, source_entity_id, entity_map):
        source_entity = self.vertices[source_entity_id]

        if source_entity:
            destination_entity_id = 10000+source_entity.entity_id

            node_data = {
                "entity_id": destination_entity_id,
                "name": source_entity.name
            }
            if hasattr(source_entity, "description"):
                node_data["description"] = source_entity.description

            cloned_node = self.add_vertex(node_data)

            if cloned_node:

                entity_map[cloned_node.entity_id] = cloned_node

                for neighbour in source_entity.neighbours:
                    entity = entity_map[neighbour.entity_id] if neighbour.entity_id in entity_map else None
                    if entity is None:
                        entity = self.clone_entity(neighbour.entity_id, entity_map)

                    cloned_node.add_neighbour(entity)

                return cloned_node

            return entity_map[node_data["entity_id"]]

    # This functions prints vertices as entities and edges as links in a graph
    # Output - JSON object in the form of {'entities':[], 'links':[]}
    def print_graph(self):

        entities = []
        links = []

        for v in self.vertices:
            node = self.vertices[v]
            vertex_json = {}
            vertex_json["entity_id"] = node.entity_id
            vertex_json["name"] = node.name
            if hasattr(node, "description"):
                vertex_json["description"] = node.description
            entities.append(vertex_json)


            for neighbour in node.neighbours:
                link_json = {}
                if neighbour:
                    link_json["from"] = node.entity_id
                    link_json["to"] = neighbour.entity_id
                    links.append(link_json)
        result = {
            "entities": entities,
            "links": links
        }

        print(result)
        return result
