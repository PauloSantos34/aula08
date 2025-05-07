aluno = {
    
    'Nome': 'Maria',
    'Idade': 29,
    'Curso': 'Analise de Dados'
}
print(aluno)
print(aluno['Idade'])
aluno['Nome'] = 'Pedro'
print(aluno)

if 'Tel' in aluno:
    aluno.pop('E-mail')
    print(aluno)

# aluno.clear()
# print(aluno)
    
del aluno
# print(aluno)

for chave, valor in aluno.items():
    print(chave, valor)
    