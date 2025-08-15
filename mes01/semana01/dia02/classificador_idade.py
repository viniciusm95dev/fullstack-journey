idade = int(input("Digite sua idade: "))

if idade < 0:
    print("idade Invalida!")
elif idade <= 2:
    classificacao = "Bebê"
    atividade = "Dormir e Mamar"
elif idade <= 12:
    classificacao = "Criança"
    atividade = "Brincar e Estudar"
elif idade <= 17:
    classificacao = "Adolescente"
    atividade = "Estudar e Descobrir o mundo"
elif idade <= 64:
    classificacao = "Adulto"
    atividade = "Trabalhar e Construir Família"
else:
    classificacao = "Idoso"
    atividade = "Descançar e Aproveitar a Família"

print(f"classificação: {classificacao}")
print(f"Atividade Principal: {atividade}")
