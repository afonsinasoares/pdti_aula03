# Supondo que a população de um país A seja da ordem de 80000
# habitantes com uma taxa anual de crescimento de 3% e que a população
# de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça
# um programa que calcule e escreva o número de anos necessários para
# que a população do país A ultrapasse ou iguale a população do país B,
# mantidas as taxas de crescimento.
paisA = 80000.0
paisB = 200000.0
ano = 0
while paisA < paisB:
    paisA = paisA + paisA * 0.03
    paisB = paisB + paisB * 0.015
    ano += 1
print("Quantidade de anos =", ano)
print("População do pais A", int(paisA)) #despreza as casas decimais. Função around funciona aqui.
print("População do pais B", int(paisB))