# -*- coding: utf-8 -*-
"""
Editor Spyder
"""

"""
A) Desenvolver um algoritmo que construa uma lista de tuplas com nome e salário de
 funcionários. Em seguida, o código deve recalcular os salários considerando os seguintes
 aumentos:
 • 20% para salários de até R$2.000,00;
 • 15% para salários entre R$2.000,00 e R$5.000,00;
 • 5% para salários maiores que R$5.000,00;
 Por fim, o código deve exibir o total de aumento (total dos salários novos menos o total de
 salários antigos e os nomes dos funcionários com salários menores que R$2.000,00.
 """
 
 #Ler o salario do funcionario
 def le_salario():
     while True:
         try:
             return float(input('Salário'))
         except:
             print('Valor inválido! Informe novamente')
 
#Leitura de nome e forma tupla de nome com salario
def le_funcionario():
    nome = input('Nome: ')
    salario = le_salario()
    return (nome, salario)

def aumenta_salarios(lista_funcionarios):
    total = 0
    for cont, funcionario in enumerate(lista_funcionarios):
        #Desempacota funcionario em nome e salario e aumenta o salario
        nome, salario = funcionario
        if salario <= 2000:
            salario *= 1.2
        elif salario <= 5000:
            salario *= 1.15
        else:
            salario *= 1.05
        #Soma todos os salarios atualizados
        total += salario
        #Atualiza a lista dos funcionarios em (nome, salario) com novo salario
        lista_funcionarios[cont] = (nome, salario)
    return total

def principal():
    lista_funcionarios = []
    total_antigo = 0
    while True:
        funcionario = le_funcionario()
        lista_funcionarios.append(funcionario)
        total_antigo += funcionario[1]
        resp = input('Continuar (S/N): ').lower().strip()
        if resp != 's':
            break
    total_novo = aumenta_salarios(lista_funcionarios)
    total_aumento = total_novo - total_antigo
    print('Total de aumento:', total_aumento)
    print('Funcionários com salário abaixo de R$2.000:')
    for nome, salario in lista_funcionarios:
        if salario < 2000:
            print(nome)

if __name == '__main__'
    principal()