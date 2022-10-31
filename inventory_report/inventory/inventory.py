import csv
import xmltodict
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def load_file(cls, path):
        with open(path) as file:
            if path.endswith('.csv'):
                return list(csv.DictReader(file))
            if path.endswith('.xml'):
                return xmltodict.parse(file.read())["dataset"]["record"]
            if path.endswith(".json"):
                return json.load(file)

    @classmethod
    def import_data(cls, path, report_type):
        products_list = cls.load_file(path)

        if report_type == 'simples':
            return SimpleReport.generate(products_list)
        if report_type == 'completo':
            return CompleteReport.generate(products_list)
