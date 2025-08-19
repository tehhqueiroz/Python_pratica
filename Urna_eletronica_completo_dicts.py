# -*- coding: utf-8 -*-
"""
Created on Sun Aug 17 22:05:05 2025

 Construir um simulador de urna eletrônica. Inicialmente, o simulador deve permitir o
 cadastro de candidatos. O usuário pode cadastrar quantos candidatos desejar. O cadastro
 de um candidato envolve um número e seu nome. O número deve ser armazenado em
 formato textual, mas deve possuir exatamente dois dígitos numéricos. A função isdigit() do
 tipo textual pode ser usada para verificar se o texto é um número válido. Por fim, os
 candidatos cadastrados devem ser mantidos em um dicionário (número: nome).
 Após o cadastro de candidatos, o simulador deve iniciar a votação. O simulador
deve permitir uma quantidade indeterminada de votos. Para votar, o usuário deve informar
o número do candidato. O sistema deve mostrar o nome do candidato para o usuário
confirmar. Números inválidos devem ser computados como votos nulos. Já o texto vazio
deve ser contabilizado como voto em branco. A sumarização dos votos deve ser feita
usando um dicionário. Ao término da votação, o simulador deve mostrar o total e a
porcentagem de votos de cada candidato, nulos e brancos

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
        print(f"Cadastrado: {numero} - {nome}")
    return candidatos


def votar(candidatos):
    # Monta contagem inicial: um contador para cada candidato + NULO/BRANCO
    votos = {num: 0 for num in candidatos}
    votos["NULO"] = 0
    votos["BRANCO"] = 0

    print("\n--- Início da votação ---")
    print("Dicas: ENTER em branco = voto BRANCO | 'FIM' para encerrar.\n")

    while True:
        entrada = input("Digite o número do candidato: ").strip()

        # Encerrar votação
        if entrada.upper() == "FIM":
            break

        # Voto BRANCO
        if entrada == "":
            confirma = input("Confirmar VOTO EM BRANCO? (S/N): ").strip().lower()
            if confirma == "s":
                votos["BRANCO"] += 1
                print("Voto BRANCO computado.\n")
            else:
                print("Voto cancelado.\n")
            continue

        # Checa formato (2 dígitos numéricos) e existência
        if not (len(entrada) == 2 and entrada.isdigit()) or entrada not in candidatos:
            print("Número inválido. Isso será computado como VOTO NULO.")
            confirma = input("Confirmar VOTO NULO? (S/N): ").strip().lower()
            if confirma == "s":
                votos["NULO"] += 1
                print("Voto NULO computado.\n")
            else:
                print("Voto cancelado.\n")
            continue

        # Voto válido
        nome = candidatos[entrada]
        print(f"Você digitou: {entrada} - {nome}")
        confirma = input("Confirmar voto? (S/N): ").strip().lower()
        if confirma == "s":
            votos[entrada] += 1
            print("Voto computado.\n")
        else:
            print("Voto cancelado.\n")

    return votos


def apurar(candidatos, votos):

    total_votos = sum(votos.values())
    print("\n--- Resultado da apuração ---")
    if total_votos == 0:
        print("Nenhum voto foi registrado.")
        return

    # Mostrar por candidato (ordenado pelo número)
    for numero in sorted(candidatos.keys()):
        qtd = votos.get(numero, 0)
        pct = (qtd / total_votos) * 100
        print(f"{numero} - {candidatos[numero]}: {qtd} voto(s) = {pct:.2f}%")

    # Nulos e Brancos
    nulos = votos.get("NULO", 0)
    brancos = votos.get("BRANCO", 0)
    pct_nulos = (nulos / total_votos) * 100
    pct_brancos = (brancos / total_votos) * 100

    print(f"NULOS: {nulos} voto(s) = {pct_nulos:.2f}%")
    print(f"BRANCOS: {brancos} voto(s) = {pct_brancos:.2f}%")
    print(f"TOTAL: {total_votos} voto(s)")


def main():
    print("--- Cadastro de candidatos ---")
    candidatos = cadastrar_candidatos()

    if not candidatos:
        print("Nenhum candidato cadastrado. Encerrando.")
        return

    votos = votar(candidatos)
    apurar(candidatos, votos)


if __name__ == "__main__":
    main()