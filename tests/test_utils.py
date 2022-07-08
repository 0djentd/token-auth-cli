import unittest
import copy

from token_auth_cli.utils import filter_none, filter_keys

_INPUT_DATA = {"None": None,
               "str": "",
               "int": 1}


class FilterNoneTests(unittest.TestCase):
    _OUTPUT_DATA = {"str": "",
                    "int": 1}

    def setUp(self):
        self.input_data = copy.copy(_INPUT_DATA)
        self.output_data = filter_none(self.input_data)

    def test_in(self):
        self.assertEqual(self.input_data, _INPUT_DATA)

    def test_out(self):
        self.assertEqual(self.output_data, self._OUTPUT_DATA)


class FilterKeysTests(unittest.TestCase):
    def setUp(self):
        self.input_data = copy.copy(_INPUT_DATA)

    def test_in(self):
        self.assertEqual(self.input_data, _INPUT_DATA)

    def test_out(self):
        for key in _INPUT_DATA:
            with self.subTest(key=key):
                output_data = filter_keys(self.input_data, [key])
                output_data_ok = copy.deepcopy(self.input_data)
                output_data_ok.pop(key)
                self.assertEqual(output_data, output_data_ok)
