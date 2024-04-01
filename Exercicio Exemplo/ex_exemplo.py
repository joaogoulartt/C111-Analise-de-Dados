import numpy as np

dataset = np.loadtxt(
    "Exercicio Exemplo/paises.csv", delimiter=";", dtype="str", encoding="utf-8"
)


def questao_1():  # Faça um slicing no dataset para mostrar apenas o País, Região, População e Area
    # dos paises contidos nele.
    print("Questão 1")
    print(dataset[1:, [0, 1, 2, 3]])


def questao_2():  # Conte e em seguida mostre quais são as diferentes Regiões contidas no dataset.
    print("Questão 2")
    regions = np.unique(dataset[1:, 1])
    print(len(regions))
    print(regions)


def questao_3():  # Mostre qual a taxa media de alfabetização do planeta segundo o dataset.
    print("Questão 3")
    print(np.mean(dataset[1:, 9].astype(float)))


def questao_4():  # Conte quantos  países  são  da  América  do  Norte  (NORTHERN  AMERICA)segundo este dataset.
    print("Questão 4")
    data = dataset[1:, 1]
    northenAmerica = np.char.find(data, "NORTHERN AMERICA")

    print(len(data[northenAmerica >= 0]))


def questao_5():  # Encontre qual país da América do Sul e Caribe (LATIN AMER. & CARIB)possui a maior renda
    # per capita(GDP ($ per capita));
    print("Questão 5")
    data = dataset[1:, 1]
    coutries = dataset[1:, 0]
    latinAmerica = np.char.find(data, "LATIN AMER. & CARIB")
    latinAmericaCountries = coutries[latinAmerica >= 0]
    latinAmericaGDP = dataset[1:, 8].astype(float)
    latinAmericaGDP = latinAmericaGDP[latinAmerica >= 0]
    print(latinAmericaCountries[np.argmax(latinAmericaGDP)])

def main():
    questao_1()
    questao_2()
    questao_3()
    questao_4()
    questao_5()


main()
