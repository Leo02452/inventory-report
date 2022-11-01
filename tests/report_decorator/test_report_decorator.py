import pytest

from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


@pytest.fixture
def products_list_mock():
    return [
        {
            "id": "1",
            "nome_do_produto": "Nicotine Polacrilex",
            "nome_da_empresa": "Target Corporation",
            "data_de_fabricacao": "2021-02-18",
            "data_de_validade": "2023-09-17",
            "numero_de_serie": "CR25 1551 4467 2549 4402 1",
            "instrucoes_de_armazenamento": "instrucao 1"
        },
        {
            "id": "2",
            "nome_do_produto": "fentanyl citrate",
            "nome_da_empresa": "Target Corporation",
            "data_de_fabricacao": "2020-12-06",
            "data_de_validade": "2023-12-25",
            "numero_de_serie": "FR29 5951 7573 74OY XKGX 6CSG D20",
            "instrucoes_de_armazenamento": "instrucao 2"
        },
        {
            "id": "3",
            "nome_do_produto": "NITROUS OXIDE",
            "nome_da_empresa": "Galena Biopharma",
            "data_de_fabricacao": "2020-12-22",
            "data_de_validade": "2024-11-07",
            "numero_de_serie": "CZ09 8588 0858 8435 9140 2695",
            "instrucoes_de_armazenamento": "instrucao 3"
        },
        {
            "id": "4",
            "nome_do_produto": "Norepinephrine Bitartrate",
            "nome_da_empresa": "Cantrell Drug Company",
            "data_de_fabricacao": "2020-12-24",
            "data_de_validade": "2025-08-19",
            "numero_de_serie": "MT04 VJPY 0772 3DCE K8U3 WIVL VV3K AEN",
            "instrucoes_de_armazenamento": "instrucao 4"
        },
    ]


def test_decorar_relatorio(products_list_mock):
    red = "\033[31m"
    green = "\033[32m"
    blue = "\033[36m"
    reset_color = "\033[0m"

    colored_report = ColoredReport(SimpleReport)
    report = colored_report.generate(products_list_mock)

    assert f"{green}Data de fabricação mais antiga:{reset_color}" in report
    assert f"{blue}2020-12-06{reset_color}" in report

    assert f"{green}Data de validade mais próxima:{reset_color}" in report
    assert f"{blue}2023-09-17{reset_color}" in report

    assert f"{green}Empresa com mais produtos:{reset_color}" in report
    assert f"{red}Target Corporation{reset_color}" in report
