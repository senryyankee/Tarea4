#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <math.h>
void u_inicial(double *onda,double numero_x, double intervalo);
void cambiar_u(double *pasado, double *presente,double numero_x,double r);
void copia(double *futuro, double *copia,double numero_x);
void dar_u(FILE *datos, double *u, double numero_x, double intervalo);

int main()
{

    FILE *datos;
    datos=fopen("datos.dat","w");
    {
    double xf=2.0;
    double tf=0.3;
    double numero_x=100.0;
    double nt=300.0;

    double intervalo=xf/numero_x;
    double dt=tf/nt;

    double c=1.0;
    const double r=c*dt/intervalo;

    double *presente = malloc(numero_x*sizeof(double));
    double *pasado = malloc(numero_x*sizeof(double));

    u_inicial(presente,numero_x,intervalo);


    for(int j=0;j<nt;j++)
    {

        for(int i=1;i<numero_x-1;i++)
        {
            pasado[i] = presente[i] - r*(presente[i]-presente[i-1]);
        }

        copia(presente,pasado,numero_x);
    }

    dar_u(datos,pasado,numero_x,intervalo);
    }
    fclose(datos);
}




void u_inicial(double *onda,double numero_x, double intervalo)
{
    int i;
    for(i=0;i<numero_x;i++)
    {
        double x=i*intervalo;
        if(0.7 < x && x < 1.2)
        {
            onda[i]=2.0;
        }
        else
        {
            onda[i]=0.0;
        }
    }
}

void copia(double *futuro, double *copia,double numero_x)
{
    int i;
    for(i=0;i<numero_x;i++)
    {
        futuro[i] = copia[i];
	}
}

void cambiar_u(double *pasado, double *presente,double numero_x,double r)
{
    int i;
    for(i=1;i<numero_x-1;i++)
    {
        pasado[i] = presente[i] - r*(presente[i]-presente[i-1]);
    }
}

void dar_u(FILE *datos, double *onda, double n_x, double delta_x)
{
	int i;
	for(i=0;i<n_x+1;i++){
		fprintf(datos,"%f %f\n", i*delta_x, onda[i]);
	}
}
