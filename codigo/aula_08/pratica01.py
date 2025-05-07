# criar dicionario de nome produto com as seguintes informações

produtos = {
    'nome': 'Notebook',
    'preço': 3500.00,
    'estoque': 15
}
if 'estoque' in produtos:
    produtos.pop("estoque")
print(produtos)


produtos['preço'] = 4000.00
print(produtos)

print(f"{produtos['nome']}: R$ {produtos['preço']}")
