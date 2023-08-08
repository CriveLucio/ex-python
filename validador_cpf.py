from os import system as sys

print("="*30)
print("Válidador de CPF")
print("="*30)


cpf = input("Digite seu cpf: ")

def validador_cpf(cpf:str):  
    
    try:
        penultimo_dig_cpf = cpf[-2] 
        ultimo_dig_cpf = cpf[-1]
        multiplicador_1_digito = 10
        multiplicacao_cpf = 0
        cpf_formatado = ""
        result_valid_cpf = None

        for num in cpf[0:-2]:
            if num.isdigit():
                cpf_formatado += num 
                multiplicacao_cpf += int(num) * multiplicador_1_digito
                multiplicador_1_digito -= 1

        calc_cpf = multiplicacao_cpf * 10 % 11
        calc_cpf = str(calc_cpf) if calc_cpf <=9 else "0"
        multiplicador_2_digito = 11
        calc_2dig_cpf = ""

        if calc_cpf in penultimo_dig_cpf:
            multiplicacao_seg_dig_cpf  = 0 
            cpf_formatado += calc_cpf
            for dig in cpf_formatado: 
                multiplicacao_seg_dig_cpf += int(dig) * multiplicador_2_digito
                multiplicador_2_digito -= 1
            calc_2dig_cpf = multiplicacao_seg_dig_cpf * 10 % 11
            calc_2dig_cpf = str(calc_2dig_cpf) if calc_2dig_cpf <=9 else "0"
        else: 
            result_valid_cpf = "CPF digitado inválido!!"
        
        if calc_2dig_cpf in ultimo_dig_cpf and calc_cpf in penultimo_dig_cpf:
            result_valid_cpf = "CPF inserido é válido!!"
        
    except IndexError: 
        result_valid_cpf = "CPF inválido!!"
    
    return result_valid_cpf

valid_cpf = validador_cpf(cpf)
print(valid_cpf)
sys('pause')