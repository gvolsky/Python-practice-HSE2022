from converter_class import Converter
import unittest
import json

class TestCsvJsonConverter(unittest.TestCase):


    def setUp(self) -> None:
        self.csv_path = "input.csv"
        self.json_path = "output.json"
        self.converter = Converter(self.csv_path, self.json_path)

    def test_read(self):
        self.assertTrue(self.converter.read())

    def test_write(self):
        data = self.converter.read()
        written_data = self.converter.write(data)
        self.assertEqual(written_data, data)

    def test_row_to_pretty(self):
        data = self.converter.read()
        data_lib = json.dumps(data)
        self.assertEqual(data_lib, data)


if __name__ == '__main__':
    unittest.main()
