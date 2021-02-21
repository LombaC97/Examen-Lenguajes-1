
class Nodos: 
    #Inicialmente los Nodos van a tenerse a si mismos (la operacion o numero)
    #Y sus hijos que seran otro nodo de la misma clase
    def __init__(self, expresion, h_izquierdo=None, h_derecho=None):
        
        self.expresion = expresion
        self.h_izquierdo  = h_izquierdo 
        self.h_derecho = h_derecho
    
    #Basicamente se va iterando por cada uno de los nodos, siempre empezando desde la operacion principal que fue la que
    #quedo en el tope de la pila, y va bajando hasta que se quede vacia
    def operar(self):
    
        if(self.expresion == '+'):
            return int(self.h_izquierdo.operar()) + int(self.h_derecho.operar())
        elif(self.expresion == '*'):
            return int(self.h_izquierdo.operar()) * int(self.h_derecho.operar())
        elif(self.expresion == '-'):
            return int(self.h_izquierdo.operar()) - int(self.h_derecho.operar())
        elif(self.expresion == '/'):
            return int(self.h_izquierdo.operar()) // int(self.h_derecho.operar())
        else:
            return int(self.expresion)

    #Es mas complejo que operar, dado que ahora queremos ir imprimiendo en una linea la operacion escrita en in order
    #Esta operacion nuevamente se llama de manera recursiva, primero con el nodo del tope de la pila y luego
    # va bajando por ambos hijos, cada hijo llama a sus hijos, etc
    def verExpresion(self, ultimo=True):
        
        #Si existe hijo izquierdo
        if self.h_izquierdo is not None:

           #Esto es para verificar precedencia, si es necesario o no poner parentesis
            if (self.expresion == '*' or self.expresion == '/') and (self.h_izquierdo.expresion == '+' or self.h_izquierdo.expresion == '-'):
                print("(", end="")
            #Llamamos a la misma funcion con el hijo izquierdo
            self.h_izquierdo.verExpresion(False)
            #Cerramos el parentesis ya que anteriormente lo habiamos abierto
            if (self.expresion == '*' or self.expresion == '/') and (self.h_izquierdo.expresion == '+' or self.h_izquierdo.expresion == '-'):
                print(")", end="")
        
        #Es en esta parte donde se imprimen los nodos como tal, y luego va subiendo en la recursion
        if self.expresion == '*' or self.expresion == '/' or self.expresion == '+' or self.expresion == '-':
            print(" ", end="")
        #Se imprime el valor del nodo
        print (str(self.expresion),end="")

        if self.expresion == '*' or self.expresion == '/' or self.expresion == '+' or self.expresion == '-':
            print(" ", end="")


        #Y luego se imprime lo que sea que contenga el hijo derecho, y continuamos con la recursion
        if self.h_derecho is not None:

            h_suma_resta = self.h_derecho.expresion == '+' or self.h_derecho.expresion == '-'
            h_mult_div = self.h_derecho.expresion == '*' or self.h_derecho.expresion == '/'

            if (self.expresion == '*' or self.expresion == '/' and h_suma_resta) or (self.expresion == '-' and h_suma_resta) or (self.expresion == '/' and h_mult_div):
                print("(", end="")

            self.h_derecho.verExpresion(False)

            if (self.expresion == '*' or self.expresion == '/' and h_suma_resta) or (self.expresion == '-' and h_suma_resta) or (self.expresion == '/' and h_mult_div):
                print(")", end="")


        if(ultimo):
            print("\n")
    
  
