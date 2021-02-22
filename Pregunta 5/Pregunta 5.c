#include <stdio.h>
#include <time.h>



//5.a 
int recursiva(int n){
	if(n>=0 && n<25){
		return n;
	}else{
		return recursiva(n-5) + recursiva(n-10) + recursiva(n-15) + recursiva(n - 20) + recursiva(n - 25);
	}
}

//5.b
int recursiva_cola_aux(int f1, int f2, int f3, int f4, int f5, int i, int n){
	if(i == n){
		return (f1 + f2 + f3 + f4 +f5);
	} return recursiva_cola_aux(f1+f2+f3+f4+f5, f1, f2,f3, f4, i+5, n);

}

int llama_recursiva_cola(int n){
	if(n<25){
		return n;
	}else{
		int i = 25 + (n % 5);
		return recursiva_cola_aux(i -5, i-10, i-15, i-20, i-25, i ,n);
	}
}

//5.c
int iterativa(int n){
	if(n< 25){return n;}

	int i = 25 + (n % 5);
	int t, f1 = i - 5, f2 = i - 10, f3 = i-15, f4 = i-20, f5 = i - 25;
	while(i <= n ){
		t = f1 + f2 + f3 + f4 + f5;
		f5 = f4;
		f4 = f3;
		f3 = f2;
		f2 = f1;
		f1 = t;
		i = i+5;
	}
	return f1;
}


void main(){
	clock_t t;
	double time;
	t = clock();
	printf("\nLlamada recursiva normal: %i\n", recursiva(160));
	t = clock() - t;
	time = ((double) t)/CLOCKS_PER_SEC;	
	printf("Tiempo tomado por recursividad normal en segundos %f", time);
	
	t = clock();
	printf("\nLlamada de cola: %i\n", llama_recursiva_cola(160));
	t = clock() - t;
	time = ((double) t)/CLOCKS_PER_SEC;
	printf("Tiempo tomado por recursividad de cola en segundos: %f", time);
	
	t = clock();
	printf("\nLlamada iterativa: %i\n", iterativa(160));
    t = clock() - t;
	time = ((double) t)/CLOCKS_PER_SEC;
	printf("Tiempo tomado por funcion iterativa en segundos: %f\n", time);

}