#include <stdio.h>
#include <limits.h>
#include <stdlib.h>



//5a 
int recursiva(int n){
	if(n>=0 && n<25){
		return n;
	}else{
		return recursiva(n-5) + recursiva(n-10) + recursiva(n-15) + recursiva(n - 20) + recursiva(n - 25);
	}
}

//5b
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
	printf("%i\n", llama_recursiva_cola(151));
	printf("%i\n", recursiva(151));
	printf("%i\n", iterativa(151));

}