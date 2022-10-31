from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products_list):
        products_per_company = super().get_company_products_quantity(
          products_list
        )

        products_per_company_report = "".join(
          [
            f"- {company}: {quantity}\n"
            for company, quantity in products_per_company.items()
          ]

        )

        return (
            super().generate(products_list)
            + "\nProdutos estocados por empresa:\n"
            + products_per_company_report
        )
