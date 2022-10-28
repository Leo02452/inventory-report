from inventory_report.inventory.product import Product


def test_cria_produto():
    new_product = Product(
        1,
        'any-name',
        'any-company',
        'any-fabric-date',
        'any-validation-date',
        'any-serie-number',
        'any-instructions'
    )

    assert new_product.__repr__() == "O produto any-name" \
        " fabricado em any-fabric-date" \
        " por any-company com validade" \
        " até any-validation-date" \
        " precisa ser armazenado any-instructions."
