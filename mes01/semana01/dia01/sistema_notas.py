print("=== SISTEMA DE NOTAS ESCOLARES ===")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"Sua média é: {media:.2f}")

if media >= 7:
    print("Parabéns! Você foi aprovado.")
elif media >= 5:
    print("Você está de recuperação.")
else:
    print("Infelizmente, você foi reprovado.")  

print("=== FIM DO SISTEMA DE NOTAS ===")
print("Desenvolvido por [M95dev] - 2025")