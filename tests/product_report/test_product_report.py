from inventory_report.inventory.product import Product


def test_relatorio_produto():
    new_product = Product(
        1,
        'any-name',
        'any-company',
        '11/12/2001',
        '11/12/2021',
        'any-serie-number',
        'any-instructions'
    )

    assert new_product.__repr__() == "O produto any-name" \
        " fabricado em 11/12/2001" \
        " por any-company com validade" \
        " até 11/12/2021" \
        " precisa ser armazenado any-instructions."
