import buddy

def main():
    print("Bienvenido al manejador de memoria pirata")
    while True:
        try:
            bloques = int(input("Por favor introduzca el numero de bloques a manejar: "))
            if(bloques >= 1):
                break
            print("El minimo a introducir es 1")
        except:
            print("Por favor introduzca un numero entero!")
    miArbol = buddy.ArbolBinario(2 ** bloques)
    while True:
        opcion = input("Introduzca RESERVAR para reserservar espacio en memoria, LIBERAR para liberar espacio, MOSTRAR para mostrar el estado actual de la memoria o SALIR para finalizar el programa ")
        
        if opcion.lower() == 'reservar':
            try:
                num_bloques = int(input("Introduzca el numero de bloques a reservar: "))
            except:
                print("Numero de bloques inválido, volviendo al menu principal")
            etiqueta = input("Introduzca la etiqueta del programa a reservar la memoria: ")
            miArbol.agregar(num_bloques, etiqueta)
        elif opcion.lower() == 'liberar':
            etiqueta = input("Introduzca la etiqueta del programa a liberar los bloques de memoria: ")
            miArbol.liberar(etiqueta)
        elif opcion.lower() == 'mostrar':
            miArbol.printArbol(miArbol.raiz)
        elif opcion.lower() == 'salir':
            break
        else:
            print("Introduzca una opcion valida")
            

if __name__ == '__main__':
    main()