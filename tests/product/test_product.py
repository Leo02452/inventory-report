from inventory_report.inventory.product import Product


def test_cria_produto():
    new_product = Product(
        1,
        'any-name',
        'any-company',
        '11/12/2001',
        '11/12/2021',
        'any-serie-number',
        'any-instructions'
    )

    assert new_product.id == 1
    assert new_product.nome_do_produto == 'any-name'
    assert new_product.nome_da_empresa == 'any-company'
    assert new_product.data_de_fabricacao == '11/12/2001'
    assert new_product.data_de_validade == '11/12/2021'
    assert new_product.numero_de_serie == 'any-serie-number'
    assert new_product.instrucoes_de_armazenamento == 'any-instructions'
