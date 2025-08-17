import random

while True:
    print("\n=== MENU DE ALGORITMOS ===")
    print("1. CALCULADORA DE IMC")
    print("2. SISTEMA DE LOGIN")      
    print("3. CALCULADORA DE DESCONTO")
    print("4. CLASSIFICADOR DE IDADE")
    print("5. SISTEMA DE NOTAS")
    print("6. PEDRA, PAPEL E TESOURA")
    print("0. SAIR")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n=== CALCULADORA DE IMC ===")
        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite sua altura em metros: "))  

        imc = peso / (altura ** 2)

        if imc < 18.5:
            classificacao = "Abaixo do peso"    
        elif 18.5 <= imc < 25:
            classificacao = "Peso normal"   
        elif imc < 30:
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obesidade"

        print(f"Seu IMC é: {imc:.2f}")
        print(f"Classificação: {classificacao}")
        print("=== FIM DA CALCULADORA DE IMC ===")

    elif opcao == "2":
        print("\n=== SISTEMA DE LOGIN ===")
        usuario_correto = "admin"
        senha_correta = "12345"

        usuario = input("Login: ")
        senha = input("Senha: ")

        if usuario == usuario_correto and senha == senha_correta:
            print("LOGIN REALIZADO COM SUCESSO!")
            print("Bem-vindo ao sistema!")

        elif usuario == usuario_correto:
            print ("SENHA INCORRETA!")
        elif senha == senha_correta:
            print("USUÁRIO INCORRETO!")
        else: 
            print("USUÁRIO E SENHA INCORRETOS!")
            print("=== FIM DO SISTEMA DE LOGIN ===")

    elif opcao == "3":
        print("\n=== CALCULADORA DE DESCONTO ===")
        preco_original = float(input("Digite o preço original: R$ "))
        desconto = float(input("Digite a porcentagem de desconto: "))
        
        valor_desconto = preco_original * (desconto / 100)
        preco_final = preco_original - valor_desconto
        
        print(f"Preço original: R$ {preco_original:.2f}")
        print(f"Desconto de {desconto}%: R$ {valor_desconto:.2f}")
        print(f"Preço final: R$ {preco_final:.2f}")
        print("=== FIM DA CALCULADORA DE DESCONTO ===")

    elif opcao == "4":
        print("\n=== CLASSIFICADOR DE IDADE ===")
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
            
        print(f"Idade: {idade} anos")
        print(f"Classificação: {classificacao}")
        print("=== FIM DO CLASSIFICADOR DE IDADE ===")

    elif opcao == "5":
        print("\n=== SISTEMA DE NOTAS ===")
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        nota3 = float(input("Digite a terceira nota: "))
        
        media = (nota1 + nota2 + nota3) / 3
        
        if media >= 7:
            situacao = "Aprovado"
        elif media >= 5:
            situacao = "Recuperação"
        else:
            situacao = "Reprovado"
            
        print(f"Nota 1: {nota1}")
        print(f"Nota 2: {nota2}")
        print(f"Nota 3: {nota3}")
        print(f"Média: {media:.2f}")
        print(f"Situação: {situacao}")
        print("=== FIM DO SISTEMA DE NOTAS ===")

    elif opcao == "6":
        print("\n=== PEDRA, PAPEL E TESOURA ===")
        opcoes = ["pedra", "papel", "tesoura"]
        
        print("Escolha: 1-Pedra, 2-Papel, 3-Tesoura")
        escolha_jogador = input("Sua escolha: ")
        
        if escolha_jogador in ["1", "2", "3"]:
            jogador = opcoes[int(escolha_jogador) - 1]
            computador = random.choice(opcoes)
            
            print(f"Você escolheu: {jogador.capitalize()}")
            print(f"Computador escolheu: {computador.capitalize()}")
            
            if jogador == computador:
                resultado = "Empate!"
            elif (jogador == "pedra" and computador == "tesoura") or \
                 (jogador == "papel" and computador == "pedra") or \
                 (jogador == "tesoura" and computador == "papel"):
                resultado = "Você ganhou!"
            else:
                resultado = "Você perdeu!"
                
            print(f"Resultado: {resultado}")
        else:
            print("Opção inválida!")
        print("=== FIM DO JOGO ===")

    elif opcao == "0":
        print("\nObrigado por usar nossos algoritmos!")
        print("Desenvolvido por [M95dev] - 2025")
        break

    else:
        print("\nOpção inválida! Tente novamente.")

    input("\nPressione Enter para continuar...")

