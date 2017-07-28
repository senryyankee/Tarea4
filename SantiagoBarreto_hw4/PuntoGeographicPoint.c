#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int main
{

}

void leerDatos(double **posicion)
{

	char *delimiter=" ";

	FILE* f = fopen("map_data.txt", "r");

	char data[10000];
	char * pch;
	int i;
	int j=0;
	while(fscanf(f, "%s",data)==1)
	{


			pch = strtok(data," ");
			posicion[j/744][j%744]=atof(pch);

			j++;
	}
	pch=strtok(NULL, " ");


	fclose(f);

}
