from os import system as sys

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
acertos = 0
for indice in perguntas: 
    print(indice['pergunta'])
    opcoes = indice['opcoes']

    for i, opcao in enumerate(indice['opcoes']):
        print(f'({i}) {opcao}')    
    while True:
        try: 
            opc_selec = int(input('Qual a opção selecionada? '))
            
        
            if opcoes[opc_selec] == indice['resposta']:
                sys('cls')
                print('Resposta correta!')
                acertos +=1

            else: 
                sys('cls')
                print('Opção incorreta.')

            break

        except ValueError:
            print('Opção selecionara inválida, por favor, digite o valor inteiro correspondente a opção desejada.')
        except IndexError: 
            print('Por favor, digite apenas o valor inteiro correspondente a opção desejada!')
        except KeyboardInterrupt:
            continue
    

print(f"Você conseguiu {acertos} acertos de {len(perguntas)} perguntas!")
sys('pause')