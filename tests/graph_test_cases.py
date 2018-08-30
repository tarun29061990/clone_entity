import sys
import os
import unittest
from unittest import TestCase

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "../")

from main import Main
from graph import Graph, Vertex


class GraphTestCase(TestCase):
    def setUp(self):
        self.graph = Graph()
        return

    def test_add_vertex(self):
        print("Running test cases for adding vertex to a graph", end='\n \n')


        node_data = {
            "entity_id": 3,
            "name": "EntityA",
            "description": "More details about entity A"
	    }

        new_vertex = self.graph.add_vertex( node_data )

        self.assertEqual(new_vertex.entity_id, 3)

    def test_add_edge(self):
        print("Running test case for adding edge between two entities with ids 3 and 5", end='\n \n')

        node_data_A = {
            "entity_id": 3,
            "name": "EntityA",
            "description": "More details about entity A"
        }

        node_data_B = {
            "entity_id": 5,
            "name": "EntityB"
	    }

        self.graph.add_edge(node_data_A["entity_id"], node_data_B["entity_id"])

        self.assertEqual(self.graph.is_neighbour(node_data_A["entity_id"], node_data_B["entity_id"]), True)

    def test_clone_entity(self):
        print("Running test for cloning entity with entity id 3", end='\n \n')

        node_data = {
            "entity_id": 3,
            "name": "EntityA",
            "description": "More details about entity A"
        }


        self.graph.add_vertex(node_data)
        cloned_entity = self.graph.clone_entity(3, {})

        self.assertEqual(10003, cloned_entity.entity_id)

    def test_print_graph(self):
        print("Running test for printing entity graph", end='\n \n')

        input_data = {'entities': [{'entity_id': 3, 'name': 'EntityA'}, {'entity_id': 5, 'name': 'EntityB'}, {'entity_id': 7, 'name': 'EntityC', 'description': 'More details about entity C'}, {'entity_id': 11, 'name': 'EntityD'}], 'links': [{'from': 3, 'to': 7}, {'from': 3, 'to': 5}, {'from': 5, 'to': 7}, {'from': 7, 'to': 11}]}


        self.graph = Main().create_entity_graph(self.graph, input_data)

        res = self.graph.print_graph()

        self.maxDiff = None
        self.assertCountEqual(res, input_data)

    def tearDown(self):
        return