perguntas = [
    {
        'pergunta': "Quem descobriu o Brasil?",
        'opcoes': ['Pedro Alvarez Cabral', 'Vasco da Gama', 'Napoleão','Cristovão Colombo'],
        'resposta': 'Pedro Alvarez Cabral',
    },
    {
        'pergunta': 'Quanto é 5 x 5?',
        'opcoes': ['25', '20', '15', '30'],
        'resposta': '25' 
    },
    {
        'pergunta': 'Qual a raiz quadrada de 16?',
        'opcoes' : ['4', '2', '8', '32'],
        'resposta': '4'
    }
]

for indice in perguntas: 
    for pergunta in indice: 
        print(indice['pergunta'])
        opcao = input('Qual a opção correta?\n(a)', indice['opcoes'[0]])