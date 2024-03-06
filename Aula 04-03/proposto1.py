import numpy as np

def questao_1():  # Crie um array com 21 elementos com valores linearmente espaçados entre 0 e 1
    print("Questão 1")
    array = np.linspace(0, 1, 21)
    print(array)
    print("\n")


def questao_2():  # Crie dois arrays: um de números pares de 0 até 51 e outro também de números pares 100 até 50.
    # Em seguida, concatene os dois arrays e mostre o resultado ordenado.
    print("Questão 2")
    array1 = np.arange(0, 52, 2)
    print("array1:", array1)
    array2 = np.arange(100, 49, -2)
    print("array2:", array2)
    conc_array = np.concatenate((array1, array2))
    print("conc_array:", np.sort(conc_array))
    print("\n")
    questao_3(conc_array)


def questao_3(array):  # Ordene o array anterior de forma decrescente.
    print("Questão 3")
    print("Array decrescente:",np.flip(np.sort(array)))
    print("\n")


def questao_4():  # Crie uma matriz formada somente por uns de tamanho 3x4. Em seguida, transforme-a em um Array 1-D.
    print("Questão 4")
    matriz = np.ones((3, 4))
    print("Matriz:", matriz)
    array = matriz.reshape(1, 12)
    print("Array:",array)
    print("\n")


def questao_5():  # Crie uma matriz identidade de tamanho qualquer. Extraia seu número de linhas e colunas,
    # multiplique-os, e diga se esta matriz poderia se tornar um vetor com número par ou impar de elementos.
    print("Questão 5")
    matriz = np.identity(5)
    print("Matriz: ", matriz)
    linhas, colunas = matriz.shape
    print("Linhas * Colunas = ", linhas * colunas)
    is_even = (linhas * colunas) % 2 == 0
    print("Vetor com número", "par" if is_even else "ímpar", "de valores após a transformação.")
    print("\n")


def main():
    print("Aula 04-03 - Exercícios Propostos 1")
    print("\n")
    questao_1()
    questao_2()  # A função questao_3 é chamada dentro da função questao_2
    questao_4()
    questao_5()

main()