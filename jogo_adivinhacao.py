import random

print("Bem-vindo ao jogo de adivinhação!")
numero_secreto = random.randint(1, 10)
tentativas = int(input("Adivinhe um número de 1 a 10: "))

if tentativas == numero_secreto:
    print("Parabéns! Você acertou o número!")   
elif tentativas < numero_secreto:
    print(f"Você errou! O número secreto era {numero_secreto}.")
else:
    print(f"Você errou! O número secreto era {numero_secreto}.")

print("Obrigado por jogar!")
print("Desenvolvido por [M95dev] - 2025")
