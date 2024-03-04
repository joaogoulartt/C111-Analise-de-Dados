aluno = {}

# Recebe os dados de um aluno e os adiciona ao dicionário
nome = input("Nome: ")
nota = input("Nota: ")
situacao = "AP" if float(nota) >= 60 else "RP"
aluno[nome] = {"nome": nome, "nota": nota, "situacao": situacao}

print(f'Aluno: {aluno[nome]}')