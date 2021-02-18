#include <stdio.h>
#include <limits.h>
#include <stdlib.h>


int **pointerA, **pointerB;
int colA, filA, colB, filB;
//Matrices del Input

//Basicamente consiste en el menu principal, se pide al usuario las dimensiones y
//Numeros a ingresar en cada matriz, y luego se reserva el espacio dinamicamente
//Asigna a los apuntadores los valores de los apuntadores a la matrizs
void matrixCreator(){
	
	printf("Introduzca el numero de filas de la matriz A: ");
	scanf("%i", &filA);
	printf("Introduzca el numero de columnas de la matriz A: ");
	scanf("%i", &colA);
	printf("Introduzca el numero de filas de la matriz B: ");
	scanf("%i", &filB);
	printf("Introduzca el numero de columnas de la matriz B: ");
	scanf("%i", &colB);
	if(colA != filB){
		printf("Tamanos de matrices no validos \n");
		exit(1);
	}

	pointerA = (int**) malloc(sizeof(int*)*filA);
	for(int i=0; i<filA; i++){
		pointerA[i] = (int * ) malloc(sizeof(int)* colA);
	}

	for(int i=0; i< filA; i++){
		for(int j= 0 ; j< colA; j++){
			printf("\nIntroduzca el valor de la fila %i columna %i de la matriz A ", i, j);
			scanf("%i", &pointerA[i][j]);
		}
	}
	
	pointerB = (int**) malloc(sizeof(int*)*filB);

	for(int i=0; i<filB; i++){
		pointerB[i] = (int * ) malloc(sizeof(int)* colB);
	}

	for(int i=0; i< filB; i++){
		for(int j= 0 ; j< colB; j++){
			printf("\nIntroduzca el valor de la fila %i columna %i de la matriz B ", i, j);
			scanf("%i", &pointerB[i][j]);
		}
	}
}
//MatrixCalculator crea el espacio dinamicamente para la matriz resultante
//Realiza las operaciones y finalmente devuelve un apuntador a la matriz para poder
//Imprimirla posteriormente
int ** matrixCalculator(){
	int suma;
	int **result;
    result = (int**) malloc(sizeof(int*)*filA);
	for(int i=0; i < filA; i++){
	    result[i] = (int * ) malloc(sizeof(int)* colB);
	}


	for(int a = 0; a < colB; a++){
		for(int i= 0; i< filA; i++){
			suma = 0;
			for(int j= 0; j< colA; j++ ){
				suma+= pointerA[i][j] * pointerB[j][a];
			}

		  result[i][a] = suma;

		}
	}

	return result;
}

void matrixPrinter(int** pointerC){
	for(int i=0; i< filA; i++){
		for(int j=0; j< colB; j++){
			printf("%d ", pointerC[i][j]);
		}
		printf("\n");
	}
}

void main(){
	int ** pointerC;
	//Lamamos a la funcion de crear matriz, crea la matriz de manera dinamica
	matrixCreator();
	//Calculamos la matriz del producto y almacenamor el valor del apuntador
	pointerC = matrixCalculator();
	//Imprimimos la matriz resultante
	matrixPrinter(pointerC);

     
	//Liberamos toda la memoria utilizada
	for(int i=0; i<filA; i++){
		free(pointerA[i]);
	}
	for(int i=0; i<filB; i++){
		free(pointerB[i]);
	}
	for(int i=0; i<filA; i++){
		free(pointerC[i]);
	}
	free(pointerC);
	free(pointerB);
	free(pointerA);


}
