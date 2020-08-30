# Faça um programa que leia e valide as seguintes informações:
# A. Nome: maior que 3 caracteres;
# B. Idade: entre 0 e 150;
# C. Salário: maior que zero;
# D. Sexo: 'f' ou 'm';
# E. Estado Civil: 's', 'c', 'v', 'd';

# validação nome
nome = ""
while len(nome) <= 3:
    nome = input("Digite o nome: ")
    if len(nome) <= 3:
        print("Nome inválido, digite novamente!")

#validação idade
idade_invalida = False
while idade_invalida:
    idade = input("Digite a idade entre 0 e 150: ")
    idade_invalida = idade < 0 or idade > 150
    if idade_invalida:
        print("Idade inválida, digite novamente!")

#validação do salário
salario = -1
