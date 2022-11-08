import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.importer.json_importer import JsonImporter


def get_importer_by_file_type(path):
    if path.endswith(".csv"):
        return CsvImporter
    if path.endswith(".xml"):
        return XmlImporter
    if path.endswith(".json"):
        return JsonImporter


def main():
    try:
        path, report_type = sys.argv[1:]
        importer = get_importer_by_file_type(path)
        inventory = InventoryRefactor(importer)
        sys.stdout.write(inventory.import_data(path, report_type))
    except ValueError:
        sys.stderr.write("Verifique os argumentos\n")
