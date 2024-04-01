import numpy as np

dataset = np.loadtxt(
    "Aula 04-03/proposto3/space.csv", delimiter=";", dtype="str", encoding="utf-8"
)

def questao_1(): #Apresente a porcentagem de missões bem sucedidas.
    statusColumn = dataset[1:, 7]
    missionSuccess = dataset[1:, 7] == "Success"
    filteredStatusColumn = statusColumn[missionSuccess]
    print("Número de missões bem sucedidas:")
    print(len(filteredStatusColumn))

def questao_2(): # Qual a média de gastos de uma missão espacial se baseando em missões que
    # tiveram gastos maiores que 0.
    costColumn = dataset[1:, 6].astype(np.float64)
    costAvailable = costColumn > 0
    filteredCostColumn = costColumn[costAvailable]
    print("Custo médio de missões espaciais:")
    print(np.mean(filteredCostColumn))

def questao_3(): #Encontre quantas missões espaciais neste DataSet foram realizadas pelos EUA
    locationColumn = dataset[1:, 2]
    USAPositionsInStrings = np.char.find(locationColumn, "USA")
    USAMissions = locationColumn[USAPositionsInStrings >= 0]
    print("Número de missões feitas pelos EUA:")
    print(len(USAMissions))

def questao_4(): # Encontre qual foi a missão mais cara realizada pela empresa "SpaceX"
    costColumn = dataset[1:, 6].astype(np.float64)
    companyColumn = dataset[1:, 1]
    spaceXLines = np.char.find(companyColumn, "SpaceX") >= 0
    spaceXCosts = costColumn[spaceXLines]
    maxCostSpaceX = max(spaceXCosts)
    print("Custo máximo de missão feita pela SpaceX:")
    print(maxCostSpaceX)

def questao_5(): # Mostre o nome da empresa e a quantidade de missões espaciais realizadas por cada uma.
    companyColumn = dataset[1:, 1]
    companiesName, numberMissions = np.unique(companyColumn, return_counts=True)
    print("Empresas e números de missões concluidas:")
    for name, numMissions in zip(companiesName, numberMissions):
        print(f"Empresa: {name} - Número de missões: {numMissions}")

def main():
    print("Aula 04-03 - Exercícios Propostos 3")
    print("\n")
    questao_1()
    questao_2()
    questao_3()
    questao_4()
    questao_5()

main()