nota = float(input("Digite a nota do aluno (0 - 10): "))
if nota < 0 or nota > 10:
    print("Nota inválida. Por favor, digite uma nota entre 0 e 10.")
elif nota >= 9:
    conceito = "A"
    status = "EXELENTE"
elif nota >= 8:
    conceito = "B"
    status = "BOM"
elif nota >= 7:
    conceito = "C" 
    status = "REGULAR"
elif nota >= 6:
    conceito = "D"      
    status = "INSUFICIENTE"
else:
    conceito = "F"
    status = "REPROVADO"

print(f"Nota: {nota}")
print(f"Conceito: {conceito}")
print(f"Status: {status}")

