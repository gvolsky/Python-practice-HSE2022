import requests
import json
import datetime


def read_data(path):
    with open(path, 'r') as f:
        content = json.loads(f.read())
    return content

def write(path, content):
    with open(path, 'w') as f:
        json_string = json.dumps(content)
        f.write(json_string)

def get_request(year, month):
    url = """https://isdayoff.ru/api/getdata?year={}&month={}&delimeter= """.format(year, month)
    response = requests.request('GET', url=url)
    content = response.content.decode('utf-8')
    return content

def count_days(content):
    days = map(int, content.split(' '))
    return days.count(0)

def calc_monthly_salary(salary, n):
    return round(salary / n, 2)

def convert_month_to_number(month):
    return datetime.datetime.strptime(month.upper(), "%B").month

def main():
    read_data_path = 'input.json'
    write_path = 'output.json'
    json_content = read_data(read_data_path)
    content = get_request(json_content['year'], convert_month_to_number(json_content['month']))
    daily_salary = calc_monthly_salary(json_content['salary'], count_days(content))
    json_content['hour_income'] = daily_salary
    write(write_path, json_content)


if __name__ == '__main__':
    main()
