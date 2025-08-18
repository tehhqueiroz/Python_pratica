# -*- coding: utf-8 -*-
"""
Created on Sun Aug 17 22:05:05 2025

 Construir um simulador de urna eletrônica. Inicialmente, o simulador deve permitir o
 cadastro de candidatos. O usuário pode cadastrar quantos candidatos desejar. O cadastro
 de um candidato envolve um número e seu nome. O número deve ser armazenado em
 formato textual, mas deve possuir exatamente dois dígitos numéricos. A função isdigit() do
 tipo textual pode ser usada para verificar se o texto é um número válido. Por fim, os
 candidatos cadastrados devem ser mantidos em um dicionário (número: nome).
 
 Montando inicialmente a função de cadastro
"""

def cadastrar_candidatos():
    candidatos = {}
    while True:
        numero = input("Número do candidato (2 dígitos) ou ENTER para finalizar: ").strip()
        if numero == "":
            break

        if not (len(numero) == 2 and numero.isdigit()):
            print("Número inválido. Digite exatamente 2 dígitos (ex.: 01, 27).")
            continue

        if numero in candidatos:
            print("Já existe candidato com esse número. Escolha outro.")
            continue

        nome = input("Nome do candidato: ").strip()
        if not nome:
            print("Nome não pode ser vazio.")
            continue

        candidatos[numero] = nome
        print('Cadastrado:', numero, '-', nome)
    return candidatos


        
if __name__ == '__main__':
    candidatos = cadastrar_candidatos()
    print(candidatos)
    
    