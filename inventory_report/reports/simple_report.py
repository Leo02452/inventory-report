from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(cls, products_list):
        oldest_manufac_date = cls.get_oldest_manufacture_date(products_list)
        closest_expire_date = cls.get_closest_expire_date(products_list)
        company_with_more_products = cls.get_company_with_more_products(
            products_list
        )

        return (
            f"Data de fabricação mais antiga: {oldest_manufac_date}\n"
            f"Data de validade mais próxima: {closest_expire_date}\n"
            f"Empresa com mais produtos: {company_with_more_products}"
        )

    @classmethod
    def get_oldest_manufacture_date(cls, products_list):
        return min(
            [product['data_de_fabricacao'] for product in products_list]
        )

    @classmethod
    def get_closest_expire_date(cls, products_list):
        return min(
            [
                product['data_de_validade']
                for product in products_list
                if product['data_de_validade'] > str(datetime.today().date())
            ]
        )

    @classmethod
    def get_company_with_more_products(cls, products_list):
        company_products_quantity = {}

        for product in products_list:
            company = product['nome_da_empresa']
            company_products_quantity[company] = company_products_quantity.get(
                company,
                0
            ) + 1

        return max(
            company_products_quantity,
            key=company_products_quantity.get
        )
