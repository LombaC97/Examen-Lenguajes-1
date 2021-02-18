class NodoArbol:
    def __init__(self,capacidad , ocupado = None, etiqueta = None,izquierdo=None,derecho=None,padre=None):
        self.capacidad = capacidad
        self.ocupado = ocupado
        self.etiqueta = etiqueta
        self.hijoIzquierdo = izquierdo
        self.hijoDerecho = derecho
        self.padre = padre


  #  def reemplazarDatoDeNodo(self,clave,valor,hizq,hder):
  ##      self.clave = clave
   #     self.cargaUtil = valor
   #     self.hijoIzquierdo = hizq
    #    self.hijoDerecho = hder
    #    if self.tieneHijoIzquierdo():
    #        self.hijoIzquierdo.padre = self
    #    if self.tieneHijoDerecho():
    #        self.hijoDerecho.padre = self


        

class ArbolBinario:

    def __init__(self, capacidad, etiqueta = None):
        self.raiz = NodoArbol(capacidad = capacidad, etiqueta= etiqueta )
        self.tamano = 0
        self.names = []  
        self.crearArbol(self.raiz)
        

    def longitud(self):
        return self.tamano

    def __len__(self):
        return self.tamano
    def crearArbol(self, nodoActual):        
        if(nodoActual.capacidad != 2):
            nodoActual.hijoIzquierdo = NodoArbol(capacidad= nodoActual.capacidad //2, padre = nodoActual)
            nodoActual.hijoDerecho = NodoArbol(capacidad= nodoActual.capacidad //2, padre = nodoActual)
            self.crearArbol( nodoActual.hijoIzquierdo)
            self.crearArbol( nodoActual.hijoDerecho)

    def printArbol(self, nodoActual, nivel = 0, direccion = None):
        if nodoActual == self.raiz:
            if(nodoActual.ocupado is not None):
                print(f"Soy el nodo padre. Mi capacidad es de {nodoActual.capacidad}, tengo ocupados {nodoActual.ocupado} bloques ")
            elif(self.revisarHijosPrint(nodoActual)):
                print(f"Soy el nodo padre. Ambos de mis hijos se encuentran ocupados ")  
            
            else:
                print(f"Soy el nodo padre. Mi capacidad es de {nodoActual.capacidad}, aun hay bloques libres ")

            self.raiz.padre = nodoActual      
        else:   
            for i in range(nivel):
                print("\t",end="")
            
            if(nodoActual.ocupado == -1):
                print(f"Nodo de capacidad {nodoActual.capacidad}, mi padre se encuentra ocupado por bloques de datos de etiqueta: {nodoActual.etiqueta}, mi padre es: {nodoActual.padre.etiqueta} de tamano {nodoActual.padre.capacidad}. Soy su hijo {direccion}", end="")
            elif(self.revisarHijosPrint(nodoActual) and nodoActual.capacidad != 2 and not(nodoActual.etiqueta in self.names)):
                print(f"Nodo de capacidad {nodoActual.capacidad}, ambos de mis hijos se encuentran ocupados, mi padre es: {nodoActual.padre.etiqueta} de tamano {nodoActual.padre.capacidad}. Soy su hijo {direccion}", end="")
            elif(nodoActual.ocupado is None):
                if(nodoActual.capacidad == 2):
                    print(f"Nodo de capacidad {nodoActual.capacidad}, me encuentro libre, mi padre es: {nodoActual.padre.etiqueta} de tamano {nodoActual.padre.capacidad}. Soy su hijo {direccion}", end="")
                else:           
                    print(f"Nodo de capacidad {nodoActual.capacidad}, aun tengo bloques libres, mi padre es: {nodoActual.padre.etiqueta} de tamano {nodoActual.padre.capacidad}. Soy su hijo {direccion}", end="")
            else:
                print(f"Nodo de capacidad {nodoActual.capacidad}, ocupados {nodoActual.ocupado} bloques de datos de etiqueta: {nodoActual.etiqueta}, mi padre es: {nodoActual.padre.etiqueta} de tamano {nodoActual.padre.capacidad}. Soy su hijo {direccion}", end="")
            print("\n")
        if (nodoActual.capacidad != 2):
            self.printArbol(nodoActual.hijoIzquierdo, nivel + 1, 'izquierdo')
            
            self.printArbol(nodoActual.hijoDerecho, nivel + 1, 'derecho')

    def revisarHijos(self, nodoActual): 
           
        if(nodoActual.capacidad != 2):    
            if(nodoActual.hijoIzquierdo.ocupado or nodoActual.hijoDerecho.ocupado):
                return True                
            else:
               return self.revisarHijos(nodoActual.hijoIzquierdo) or self.revisarHijos(nodoActual.hijoDerecho)               
        else:            
            if(nodoActual.ocupado):
                return True
    def revisarHijosPrint(self, nodoActual): 
           
        if(nodoActual.capacidad != 2):    
            if(nodoActual.hijoIzquierdo.ocupado and nodoActual.hijoDerecho.ocupado):
                return True                
            else:
               return self.revisarHijos(nodoActual.hijoIzquierdo) and self.revisarHijos(nodoActual.hijoDerecho)               
        else:            
            if(nodoActual.ocupado):
                return True
              

            
    def buscarInsertarArbol(self, capacidad, aOcupar, etiqueta, nodoActual, array):      
    
        if (nodoActual.capacidad == capacidad and not(nodoActual.ocupado)):
            if(nodoActual.capacidad != 2 ):
                
                if not(self.revisarHijos(nodoActual)):#     not(nodoActual.hijoIzquierdo.ocupado or nodoActual.hijoDerecho.ocupado)):
                    #if(not(nodoActual == self.raiz)):
                        #if(not(nodoActual.padre.ocupado)):     #creo que es innecesaria            
                    array.append(nodoActual) 
                    #else:
                     #   array.append(nodoActual)        
            else:            
                array.append(nodoActual)      
        else:       
            if(nodoActual.capacidad!= 2): #creo que se puede optimizar
                self.buscarInsertarArbol(capacidad, aOcupar, etiqueta, nodoActual.hijoIzquierdo, array)       
                self.buscarInsertarArbol(capacidad, aOcupar, etiqueta, nodoActual.hijoDerecho, array)
    
        return array

    def buscarLiberarArbol(self, etiqueta, nodoActual):      
        if(nodoActual.capacidad != 2):

            if( nodoActual.etiqueta == etiqueta):
                nodoActual.etiqueta = None
                nodoActual.ocupado = None
                self.names.remove(etiqueta)
                

                if(nodoActual != self.raiz and not(nodoActual.padre.hijoDerecho.ocupado or nodoActual.padre.hijoIzquierdo.ocupado)):
                    
                    nodoActual.padre.etiqueta = None
                    nodoActual.padre.ocupado = None
            
                self.liberarHijos(nodoActual.hijoIzquierdo)
                self.liberarHijos(nodoActual.hijoDerecho)
                return True
                
            else:
                return self.buscarLiberarArbol(etiqueta, nodoActual.hijoIzquierdo) or self.buscarLiberarArbol(etiqueta, nodoActual.hijoDerecho)
        else:
            if(nodoActual.etiqueta == etiqueta):
                self.names.remove(etiqueta)
                nodoActual.etiqueta = None
                nodoActual.ocupado = None
                
                if(not(nodoActual.padre.hijoDerecho.ocupado or nodoActual.padre.hijoIzquierdo.ocupado)):
                    
                    nodoActual.padre.etiqueta = None
                    nodoActual.padre.ocupado = None
                return True
        

    def agregar(self, aOcupar, etiqueta):        
        return self._agregar(aOcupar, etiqueta)       
       
    
    def ocuparHijos(self, nodoActual, etiqueta):
        nodoActual.ocupado = -1
        nodoActual.etiqueta = etiqueta
        if nodoActual.capacidad == 2:
            return 

        self.ocuparHijos(nodoActual.hijoIzquierdo, etiqueta)
        self.ocuparHijos(nodoActual.hijoDerecho, etiqueta)

    def liberarHijos(self, nodoActual):
        
        nodoActual.ocupado = None
        nodoActual.etiqueta = None
        
        if nodoActual.capacidad == 2:
            return 

        self.liberarHijos(nodoActual.hijoIzquierdo)
        self.liberarHijos(nodoActual.hijoDerecho)

    
    def _agregar(self, aOcupar, etiqueta):
        if(aOcupar > self.raiz.capacidad):
            return print("El bloque es mayor al tamaño de memoria maximo")
        if(etiqueta in self.names):
            return print("Nombre de etiqueta ya existente en memoria")
        capacidad = self.raiz.capacidad
        while True:
            if(aOcupar <= capacidad and aOcupar > capacidad // 2 ):     
                break            
            capacidad = capacidad // 2            
        if capacidad == 1:
            capacidad += 1       
             
       
        ingresado = self.buscarInsertarArbol(capacidad = capacidad, aOcupar= aOcupar, etiqueta= etiqueta, nodoActual= self.raiz, array = [])
        if(not(ingresado)):
            print("Error: no hay suficientes bloques de memoria disponibles, imposible ingresar")
                                        
        else:
            ingresado[0].ocupado = aOcupar
            ingresado[0].etiqueta = etiqueta
            self.names.append(etiqueta)
            print("Bloque ingresado correctamente")
                
            if(ingresado[0].capacidad != 2):
                self.ocuparHijos(ingresado[0].hijoIzquierdo, etiqueta)
                self.ocuparHijos(ingresado[0].hijoDerecho, etiqueta)
               #if(ingresado[0] != self.raiz): #and ingresado[0].padre.hijoDerecho.ocupado and ingresado[0].padre.hijoIzquierdo.ocupado):   #ojo creo q e se puede quitar                
                 #   ingresado[0].padre.etiqueta = 'Me ocupo uno de mis hijos'
                  #s  ingresado[0].padre.ocupado = -2
            return ingresado[0]   

    def liberar(self, etiqueta):
        if not(etiqueta in self.names):
            return print("Imposible liberar memoria de etiqueta no existente")
        return self.buscarLiberarArbol(etiqueta, self.raiz)

        


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
    miArbol = ArbolBinario(2 ** bloques)
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




