import pandas as pd

dfPaises = pd.read_csv('Aula 29-04/paises.csv', delimiter=';')

def questao1():
    print('Questão 1')
    print('-'*50)
    
    # a) Quais são os países da Oceania?
    dfOceania = dfPaises['Region'].str.contains('OCEANIA')
    print('Países da Oceania: ', dfPaises[dfOceania]['Country'].values)
    
    # b) Quantos são os países da Oceania?
    print('-'*50)
    print ('Quantidade de países da Oceania:', len(dfPaises[dfOceania]))
    print('')
    print('='*50)
    
def questao2(): # Mostre a média de taxa de alfabetização (Literacy (%)) do planeta
    print('Questão 2')
    print('-'*50)
    media = dfPaises['Literacy (%)'].mean()
    print('Média de taxa de alfabetização (Literacy (%)) do planeta: ', media.round(2))
    print('')
    print('='*50)
    
def questao3(): # Encontre o nome e a região do país que possuí a maior população
    print('Questão 3')
    print('-'*50)
    maior_populacao = dfPaises['Population'].max()
    dfMaiorPopulacao = dfPaises[dfPaises['Population'] == maior_populacao]
    print('Nome e Região do país com maior população:\n', dfMaiorPopulacao[['Country', 'Region']].values[0])
    print('')
    print('='*50)
    
def questao4(): # Busque o nome de todos os países do dataset que não possuem costa marítima 
    # (Coastline (coast/area ratio) = 0) e guarde-os em um arquivo CSV chamado 'noCoast.csv'
    print('Questão 4')
    print('-'*50)

    dfNoCoast = dfPaises[dfPaises['Coastline (coast/area ratio)'] == 0]
    dfNoCoast.to_csv(path_or_buf='Aula 29-04/noCoast.csv', index=False, )
    print('Arquivo noCoast.csv criado com sucesso!')
    
def main():
    questao1()
    questao2()
    questao3()
    questao4()
    
main()