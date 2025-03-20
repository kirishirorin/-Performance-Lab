import json
import argparse


def find_value(id, values_file):
    with open(values_file, 'r') as values:
        values_dict = json.load(values)
        for elem in values_dict['values']:
            if elem['id'] == id:
                return elem['value']


def write_into_report_file(result_dict, report_file):
    with open(report_file, 'w') as report_file:
        json.dump(result_dict, report_file, indent=2)


def make_report(values_file, tests_file):
    with open(tests_file, 'r') as tests:
        tests_dict = json.load(tests)
        report = {'tests': []}
        def inner(tests, report):
            current_report = report
            for elem in tests:
                add_to_report = {'id': elem['id'], 'title': elem['title'], 'value': find_value(elem['id'], values_file)}
                if elem.get('values', None):
                    add_to_report.update({'values': []})
                    add_to_report['values'] = inner(elem['values'], [])
                current_report.append(add_to_report)
            return current_report
        report['tests'] = inner(tests_dict['tests'], report['tests'])
        return report


def main():
    parser = argparse.ArgumentParser(description='Дополняет доклад')
    parser.add_argument('values_file', type=str)
    parser.add_argument('tests_file', type=str)
    parser.add_argument('report_file', type=str)
    args = parser.parse_args()
    report_dict = make_report(args.values_file, args.tests_file)
    write_into_report_file(report_dict, args.report_file)

if __name__ == '__main__':
    main()
