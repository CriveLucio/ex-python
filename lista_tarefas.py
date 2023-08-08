matriz = [['1', 2, "4", 12, 22],[4, "-","Sérgio", 4, 3],[9, 6.327427 ,5, "7" ,"perfume"]]
def soma_matriz(matriz):
    soma = 0
    for lista in matriz: 
        for num in lista: 
            num = validador_dados(num)
            soma += num 

    return soma

def soma_1_indice(matriz):
    soma = 0 
    for num in matriz:
        num = validador_dados(num[0])
        soma += num

    return soma

def soma_ultimo_indice(matriz):
    soma = 0 
    for num in matriz:
        num = validador_dados(num[-1])
        soma += num

    return soma

def soma_indice_meio(matriz):
    soma = 0
    tamanho_matriz = []
    var_lista = 0
   
    for matrizes in matriz:
        var_lista = int(len(matrizes) / 2)
        tamanho_matriz.append(var_lista)

    for indice,num in enumerate(matriz):
        num = num[tamanho_matriz[indice]]
        num = validador_dados(num)
        soma += num
    
    return soma 

def validador_dados(num):
    num_validado = 0
    if type(num) is str:
        if str(num).isdigit():
           num_validado = int(num)
        else:
            num_validado = 0
    
    elif type(num) is int or type(num) is float: 
        num_validado = num
    
    
            
    return num_validado
       
    
    



print(soma_matriz(matriz))
print(soma_1_indice(matriz))
print(soma_ultimo_indice(matriz))
print(soma_indice_meio(matriz))