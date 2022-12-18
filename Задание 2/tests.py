from converter_class import Converter
import unittest
import json

class TestCsvJsonConverter(unittest.TestCase):


    csv_path = "./input.csv"
    json_path = "./output.json"
    converter = Converter(csv_path, json_path)

    def test_read(self):
        self.assertTrue(self.self_converter.read_data())
        self.assertTrue(self.lib_converter.read())

    def test_write(self):
        data = self.converter.read()
        written_data = self.converter.write(data)
        check_data = self.self_converter.write_data(data)
        self.assertEqual(written_data, check_data)

    def test_row_to_pretty(self):
        data = self.converter.read()
        data_lib = json.dumps(data)
        self.assertEqual(data_lib, data)


if __name__ == '__main__':
    unittest.main()
