#include <stdio.h>
#include <limits.h>
#include <stdlib.h>

long long unsigned factorial(int x){
	if(x < 0 ){
		printf("Debe introducir un numero no negativo \n");
		exit(0);
	}
	long  long unsigned resultado = 1;
	while (x > 1){
		resultado = resultado * x;
		x --;
	}

	return resultado;

}
void main(){
	int x;
	long long unsigned number;
	printf("Introduzca el numero al que desee calcular factorial: ");
	scanf("%d", &x);
	number = factorial(x);
	if( number == 0){
		printf("El resultado es demasiado grande \n");	
	}
	else{ printf("%llu \n", number); }
	
}
