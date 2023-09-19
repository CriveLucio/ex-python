#importando biblioteca para deep copy e importando os dados
from ast import main
from copy import deepcopy
from dados import produtos

# Usar desempacotamento para aumentar o valor dos produtos em 10%]

def ajuste_preco(produtos, coeficiente):
    produtos_att = [
        {**produto, 'preco': round(produto['preco'] * coeficiente, 2)}
        for produto in produtos
        ]
    return produtos_att


coeficiente = 1.1

produtos = ajuste_preco(produtos, coeficiente)
 
# Criação de novos produtos para dentro da lista

produto_adc = input('Qual o nome do produto que deseja adcionar? ')
preco_produto_adc = input ('Qual o valor desse produto? ')
produtos.append({'nome': produto_adc, 'preco': preco_produto_adc,})

# Ordenar produtos em ordem decrescente
    
produtos_ordenados_nome_descrescente = sorted(
    deepcopy(produtos),
    key = lambda produto: produto['nome'],
    reverse= True
)


produtos_ordenados_nome = sorted(
    deepcopy(produtos),
    key = lambda produto: produto['nome']
)


produtos_ordenados_preco_descrescente = sorted(
    deepcopy(produtos),
    key = lambda produto: float(produto['preco']),
    reverse= True
)

produtos_ordenados_preco = sorted(
    deepcopy(produtos),
    key = lambda produto: float(produto['preco'])
)

print('Ordenado por nome em ordem decrescente: ', *produtos_ordenados_nome_descrescente, sep = '\n')
print('Ordenado por nome em ordem crescente: ', *produtos_ordenados_nome, sep = '\n')
print('Ordenado por preço em ordem decrescente: ', *produtos_ordenados_preco_descrescente, sep = '\n')
print('Ordenado por preço em ordem crescente: ', *produtos_ordenados_preco, sep = '\n')

