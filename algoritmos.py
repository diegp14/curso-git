#BUSQUEDA BINARIA
def busqueda_binaria(lista, elemento):
    inicio = 0
    fin = len(lista) - 1  # la ultima posicion de la lista
    while inicio <= fin:
        medio = (inicio + fin)//2
        valor_medio = lista[medio]

        if valor_medio == elemento:
            return valor_medio
        elif valor_medio < elemento:
            inicio = medio + 1
        else:
            fin = medio - 1
    return None


mi_lista = [1,2,3,4,5,6,7]
