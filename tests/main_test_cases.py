import sys
import os
import unittest
from unittest import TestCase

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../tests")
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "../")

from main import Main

class MainTestCase(TestCase):
    def setUp(self):

        return

    def test_entity_clone(self):
        print("Running test case for cloning an entity graph with given entity id", end="\n\n")
        input_file_path = 'tests/test_input.json'
        entity_id_to_be_cloned = 5

        result_data = {'entities': [{'entity_id': 3, 'name': 'EntityA'}, {'entity_id': 5, 'name': 'EntityB'}, {'entity_id': 7, 'name': 'EntityC', 'description': 'More details about entity C'}, {'entity_id': 11, 'name': 'EntityD'}, {'entity_id': 10005, 'name': 'EntityB'}, {'entity_id': 10007, 'name': 'EntityC', 'description': 'More details about entity C'}, {'entity_id': 10011, 'name': 'EntityD'}], 'links': [{'from': 3, 'to': 5}, {'from': 3, 'to': 10005}, {'from': 3, 'to': 7}, {'from': 5, 'to': 7}, {'from': 7, 'to': 11}, {'from': 10005, 'to': 10007}, {'from': 10007, 'to': 10011}]}

        res = Main().main(input_file_path, entity_id_to_be_cloned)

        self.assertDictEqual(dict(res), dict(result_data))

    def tearDown(self):
        return