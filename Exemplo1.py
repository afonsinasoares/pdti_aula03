iterador=0

while iterador <= 150:
    # pode ser assim
    # if iterador % 5 == 0
    #     print(intarador)

    # desta manteira fica mais legível
    tem_resto = iterador % 5 != 0
    if not tem_resto:
        print(iterador)
    iterador += 1
