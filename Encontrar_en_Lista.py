lista = [1, 2, 3, 4]


def imprimr_NUM(lista, num):
    if lista==[]:
        return "No existe"

    elif num == lista[0]:
        return num
    else:
        return imprimr_NUM(lista[1:], num)


print(imprimr_NUM(lista, 3))
