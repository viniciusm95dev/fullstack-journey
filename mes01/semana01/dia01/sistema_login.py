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