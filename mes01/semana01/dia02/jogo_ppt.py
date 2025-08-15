import random

opcoes = ["pedra", "papel", "tesoura"]
jogador = input("Escolha pedra, papel ou tesoura: ").lower()
computador = random.choice(opcoes)

print(f"Jogador escolheu: {jogador}")
print(f"Computador escolheu: {computador}")

if jogador not in opcoes:
    print("Opção inválida! Escolha pedra, papel ou tesoura.")

elif jogador == computador:
    print("Empate!")
elif (jogador == "pedra" and computador == "tesoura") or \
     (jogador == "papel" and computador == "pedra") or \
     (jogador == "tesoura" and computador == "papel"):
    print("Você ganhou!")
else:
    print("Você perdeu!")


