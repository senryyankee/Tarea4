#include <stdio.h>

int main()
{
	float f, c;
	float low, up, step;
	
	low=0;	
	up=300;
	step=20;
	
	f=low;
	while (f <= up)
	{
	c=(5.0/9.0) * (f-32.0) ;
	printf("%3.0f\t%6.1f\n", f, c);
	f = f + step;
	}
}
