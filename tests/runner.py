import sys
import os
import unittest
from unittest import TestCase

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../tests")
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "../")

from graph_test_cases import GraphTestCase
from main_test_cases import MainTestCase

class Runner(TestCase):
    def setUp(self):
        return

    def run_test_cases(self):
        suite1 = unittest.TestLoader().loadTestsFromTestCase(GraphTestCase)
        suite2 = unittest.TestLoader().loadTestsFromTestCase(MainTestCase)
        alltests = unittest.TestSuite([suite1, suite2])

    def tearDown(self):
        return



if __name__ == '__main__':
    unittest.main()