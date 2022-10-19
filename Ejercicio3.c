#include <stdio.h>
#include <string.h>
#include <omp.h>

char palabra[30];
int longitud;
int aux=0;
    
int main(){
    printf("Introdusca una Palabra cualquiera:");
   
    scanf("%s", palabra);
    
    #pragma omp taskwait
    {
        longitud = strlen(palabra);
    }
    
    #pragma omp parallel
    {
        for(int i=0;i < longitud ;i++){
            if(palabra[i] != palabra[longitud-i-1]){
                #pragma omp task shared(fin)
                {
                    aux = 1;
                }
                break;
           }
        }
    }
    if (aux) {
        printf("%s es Falso \n", palabra);
    }    
    else {
        printf("%s es Verdadero \n", palabra);
    }
    return 0;
} 