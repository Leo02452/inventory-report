from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor(Iterable):
    def __init__(self, importer) -> None:
        self.importer = importer
        self.data = []

    def __iter__(self):
        return InventoryIterator(self.data)

    def get_report(self, report_type):
        if report_type == 'simples':
            return SimpleReport.generate(self.data)
        elif report_type == 'completo':
            return CompleteReport.generate(self.data)

    def import_data(self, path, report_type):
        self.data.extend(self.importer.import_data(path))
        return self.get_report(report_type)
