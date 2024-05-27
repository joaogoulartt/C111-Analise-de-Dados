import pandas as pd
import matplotlib.pyplot as plt


def menu():
    print('\n' + ('=' * 50) + '\n')
    print('Digite o número da questão que deseja visualizar:')
    print('1 - Quantidade de Empresas Espaciais dos EUA e China')
    print('2 - Taxa de Natalidade e Mortalidade dos Países da América do Norte')
    print('0 - Sair\n')
    select = input('Digite o número da questão:')
    if select == '1':
        questao1()
    elif select == '2':
        questao2()
    elif select == '0':
        print('Saindo...')
        exit()
    else:
        print('Opção inválida!')
    

def questao1():  # Trace um gráfico em barras mostrando quantas empresas Espaciais os EUA e a CHINA possuem
    dfSpace = pd.read_csv('Aula 27-05/space.csv', delimiter=';')
    
    dfEUA = dfSpace[dfSpace['Location'].str.contains('USA')]['Company Name'].unique()
    dfChina = dfSpace[dfSpace['Location'].str.contains('China')]['Company Name'].unique()
    
    plt.xlabel('Países', fontsize=10)
    plt.ylabel('Quantidade de Empresas', fontsize=10)
    plt.title('Quantidade de Empresas Espaciais dos EUA e China', fontsize=12, fontweight='bold')
    
    plt.xticks(fontsize=8, rotation=0)
    plt.yticks(fontsize=8, rotation=0)
    
    plt.bar(['EUA', 'China'], [len(dfEUA), len(dfChina)])
    plt.show()

    
def questao2():  # Trace dois gráficos de linhas em um mesmo plano cartesiano, um mostrando a taxa de
    # mortalidade e outro a taxa de natalidade dos países da América do Norte.
    dfPaises = pd.read_csv('Aula 27-05/paises.csv', delimiter=';')
    
    dfNorthenAmerica = dfPaises[dfPaises['Region'].str.contains('NORTHERN AMERICA')]
    
    plt.xlabel('Países', fontsize=10)
    plt.ylabel('Taxa', fontsize=10)
    plt.title('Taxa de Natalidade e Mortalidade dos Países da América do Norte', fontsize=12, fontweight='bold')

    plt.xticks(fontsize=8, rotation=0)
    plt.yticks(fontsize=8, rotation=0)
    
    plt.plot(dfNorthenAmerica['Country'], dfNorthenAmerica['Birthrate'], 'o-b', dfNorthenAmerica['Country'], dfNorthenAmerica['Deathrate'], 'o--r')
    plt.legend(['Natalidade', 'Mortalidade'])
    
    plt.show()
    
    
def main():
    while True:
        menu()

    
main()
