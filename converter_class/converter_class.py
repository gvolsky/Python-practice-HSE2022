import json
import csv
import sys


class Converter:

    def __init__(self, inp_csv, out_json):
        self.inp = inp_csv
        self.out = out_json

    def read(self):
    	lines = []
        with open(self.inp, 'r', newline='') as f:
            return list(csv.DictReader(f, delimiter=','))

    def write(self, data):
        result = json.dumps(data)
        with open(self.out, 'w') as f:
            f.write(result)


def main():
    inp, out = sys.argv[1:3]
    converter = Converter(inp, out)
    data = converter.read()
    converter.write(data)
    

if __name__ == "__main__":
    main()
