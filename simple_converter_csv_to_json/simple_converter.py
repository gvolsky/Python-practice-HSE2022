import sys
def read_data(file_name):
    file = open(file_name)
    content = file.read()
    file.close()
    return content


def write_data(file_name, data):
    file = open(file_name, 'w')
    file.write(data)
    file.close()


def read_data_to_list(file_name):
    file = open(file_name)
    content = file.readlines()
    file.close()
    return content


def prepare_data(data):
    if data:
        title = data.pop(0).strip().split(',')
    else:
        title = []
    return title, data


def convert_row_to_pretty_json(titles, row):
    values = row.strip().split(',')
    raw_data = []
    for title, value in zip(titles, values):
    	raw_data.extend([title.strip(), value.strip()])
    data = """  {{
    {}: {},
    {}: {},
    {}: {},
    {}: {},
    {}: {}
  }}""".format(*raw_data)
    return data


def convert_csv_to_json(data):
    titles, data = prepare_data(data)
    result = []
    for row in data:
        result.append(convert_row_to_pretty_json(titles, row))
    result = ''.join(['[\n', ',\n'.join(result), '\n]'])
    return result


def main():
    inp, out = sys.argv[1:3]
    data = read_data_to_list(inp)
    result = convert_csv_to_json(data)
    write_data(out, result)


if __name__ == "__main__":
    main()
