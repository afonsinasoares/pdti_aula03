tabuada = input("Tabuada de multiplicação, digite o valor: ")
tabuada = int(tabuada)

iterador = 1
while iterador <= 10:
    resultado = iterador * tabuada
    print(tabuada,"x",iterador," = ",resultado)
    iterador +=1