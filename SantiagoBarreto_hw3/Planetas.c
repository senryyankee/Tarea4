#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

int main()
{
	double pow(double x, double y);
   	float powf(float x, float y);
   	long double powl(long double x, long double y);
	double G = 4*3.1415*3.1415;
	double sunmass = 1.989 * pow(10,30);
	
	double masas[10];
	double velocidades[10][3];
	double posiciones[10][3];

	char *delimiter=",";

	FILE* f = fopen("coordinates.csv", "r");

	char planeta[100];
	char * pch;
	int i;
	int j=0;
	while(fscanf(f, "%s",planeta)==1)
	{
		

				pch = strtok(planeta,",");

				pch = strtok(NULL,",");
				masas[j]=atof(pch);

				pch = strtok(NULL,",");
				posiciones[j][0]=atof(pch);

				pch = strtok(NULL,",");
				posiciones[j][1]=atof(pch);

				pch = strtok(NULL,",");
				posiciones[j][2]=atof(pch);

				pch = strtok(NULL,",");
				velocidades[j][0]=atof(pch);

				pch = strtok(NULL,",");
				velocidades[j][1]=atof(pch);

				pch = strtok(NULL,",");
				velocidades[j][2]=atof(pch);

			i++;
			
		j++;

	}


	fclose(f);
	
}



int aceleracion(double** R){
	int a[10][3]; 
	double masas[10]
	int i;
	for(i=0;i<10;i++){
		int j;		
		for(j=0;j<10;j++){
			int d;
			d= R[i]-R[j];
			if (i != j){
				double pow(double x, double y);
   				float powf(float x, float y);
   				long double powl(long double x, long double y);
				double th;
				th= pow((d*d), 0.5);
				th= pow(th, 3);
				a[i] += G*masas[j]*d/th;
			
			}
	
}
	
}
	

}





















