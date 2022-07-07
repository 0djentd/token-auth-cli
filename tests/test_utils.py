import unittest
import copy

from token_auth_cli.utils import filter_none

INPUT_DATA = {"None": None,
              "str": "",
              "int": 1}

OUTPUT_DATA = {"str": "",
               "int": 1}

class FilterNoneTests(unittest.TestCase):
    def setUp(self):
        self.input_data = copy.copy(INPUT_DATA)
        self.output_data = filter_none(self.input_data)

    def test_in(self):
        self.assertEqual(self.input_data, INPUT_DATA)

    def test_out(self):
        self.assertEqual(self.output_data, OUTPUT_DATA)
