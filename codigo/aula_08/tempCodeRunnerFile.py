ef cadastra_pessoa(num):
    for i in range(num):
    nome = input('Informe o nome do vendedor: ')
    valor = input('Informe o valor da venda: ')

    pessoa = {
    'Nome': nome,
    'Valor': valor

    }
    
    lst_cadastro.append(pessoa)
# Principal
lst_cadastro = []

qtd = int(input('Quantas pessoas?'))
cadastra_pessoa(qtd)
lst_cadastro = []