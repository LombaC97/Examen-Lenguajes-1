import sys
from Nodos import *

# Se crea todo el arbol con los nodos y se almacenan en una pila. Es
# la manera mas sencilla de hacerlo
def crearArbol(expresion, inverso = False):
  
    pila = []
    for letra in expresion:
        
        if (letra=='+' or letra=='-' or letra=='*' or letra=='/'):
            #Si en algun momento hay un error al querer extraer un elemento de nuestra pila
            #entonces quiere decir que la pila se quedo vacia antes de tiempo, lo que indica
            #que la expresion no era valida
            try:
                elem1 = pila.pop()            
                elem2 = pila.pop()
            except:
                return print("Expresion invalida")

            if inverso:
                pila.append(Nodos(letra,elem1,elem2))
            else:
                pila.append(Nodos(letra,elem2,elem1))        
        else:  
            #Si es un numerito, lo metemos entonces y ya
            pila.append(Nodos(letra))

    if not pila:
        return Nodos("") 
    #Al final, el arbol va a quedar en la cabeza de la pila, y sera el unico que quede
    arbol = pila.pop()
    #Si luego de finalizar de leer la expresion y haber extraido el arbol hay algo todavia en la pila, entonces la expresion
    #no era valida
    if pila:
        return print("Expresion invalida")

    return arbol


def esValida(accion, result = False):
    #Si el input es vacio o menor al tamano minimo
    
    #O tambien puede que sea SALIR
    if len(accion) == 1 and accion[0] == "SALIR":
        return True
    if (len(accion) < 3):
        return False
    #Evaluamos primero que sea una opcion valida con el formato correcto
    if( (accion[0] == "EVAL" or accion[0] == "MOSTRAR") and (accion[1] == "PRE" or accion[1] == "POST" ) and len(accion) > 3):
        result = True
    #Luego vemos si hay algo que no sea un caracter admitido en el input
    for letra in accion[2:]:
        if(not(letra.isdigit()) and letra != '+' and letra != '-' and letra != '/' and letra != '*'):
            result = False

    return result

def main():    
    while True:
        print("Ingrese la expresion que desee ejecutar: ")
        accion = sys.stdin.readline()[:-1].split(' ') 
        #Usamos listas por comprension para eliminar cualesquiera posibles espacios vacios en el arreglo      
        accion = [ele for ele in accion if ele != ''] 
        #Verificamos que sea una accion valida
        if not esValida(accion):
            print("Formato invalido")          
            continue

        if accion[0] == "SALIR":
            break
        #Evaluar la expresion en preorder, es lo mismo que invertirla y evaluarla en post orden
        if(accion[1] == "PRE"):            
            expresion = accion[2:]           
            arbol = crearArbol(reversed(expresion), True)
        else:            
            arbol = crearArbol(accion[2:])
        #Si el arbol existe, es decir, la funcion crearArbol devolvio algo
        if(arbol is not None):
            if(accion[0] == "EVAL"):
                print(arbol.operar())
            else:
                arbol.verExpresion()

if __name__ == "__main__":
    main()