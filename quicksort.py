print("Segundo archivo!!")
print("Segundo cambio!! aplicar comando diff")

#consultar los commits con 
#git log y/o git log --graph

#para crear nuestras propios comandos con git config --global alias.nombre_comando "el_comando"
#  

#version 2
def quicksort(arreglo):
    if len(arreglo)<2:
        return arreglo
    else:
        pivote = arreglo[0]
        menores = [i for i in arreglo[1:] if i<= pivote]

        mayores = [i for i in arreglo[1:] if i > pivote]
        return quicksort(menores)+[pivote]+quicksort(mayores)

print(quicksort([10,2,8,4]))