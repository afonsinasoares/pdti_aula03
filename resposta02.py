# Faça um programa que leia um nome de usuário e a sua senha e não
# aceite a senha igual ao nome do usuário, mostrando uma mensagem de
# erro e voltando a pedir as informações.
continua = True
while continua:
    nome = input("Digite o nome: ")
    senha = input("Digite a senha: ")
    if nome != senha:
        # continua = False
        break #pode ser usando o brak tb para sair do laço
    else:
        print("A senha não pode ser igual ao nome!")