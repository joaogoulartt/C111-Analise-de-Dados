import numpy as np

def questao_1():# Crie um array de floats de 10 elementos positivos e negativos ente 0 e 1. Em seguida, multiplique
    # seus valores por 100 e crie um novo vetor apenas com a parte inteira destes números.(use seed(5) antes).
    print("Questão 1")
    np.random.seed(5)
    float_array = np.random.rand(10) * 100
    print("float_array:", float_array)
    int_array = float_array.astype(int)
    print("int_array:",int_array)
    print("\n")

def questao_2(): # Crie uma matriz de 4x4 formada por números aleatórios entre 1 e 50;(use seed(10) antes)
    np.random.seed(10)
    matriz = np.random.randint(1, 51, (4, 4))
    print("Matriz:",matriz)
    print("\n")
    questao_3(matriz)

def questao_3(matriz):# Mostre o resultado da média de cada linha e coluna da matriz. Em seguida, mostre o maior valor
    # destas médias.
    print("Questão 3")
    print("")
    print("Média das linhas:", matriz.mean(axis=1))
    print("Média das colunas:", matriz.mean(axis=0))
    print(matriz.mean(axis=1))
    print(matriz.mean(axis=0))
    print(max(matriz.mean(axis=1)))
    print(max(matriz.mean(axis=0)))
    print("\n")
    questao_4(matriz)

def questao_4(matriz): # Baseado na matriz anterior, mostre a quantidade de aparições de cada número. Em seguida,
    # mostre apenas os números que aparecem 2 vezes.
    unique, counts = np.unique(matriz, return_counts=True)
    print(unique)
    print(counts)
    print(unique[counts == 2])

def main():
    print("Aula 04-03 - Exercícios Propostos 2")
    print("\n")
    questao_1()
    questao_2() # A função questao_3 e questao_4 são chamadas dentro da função questao_2