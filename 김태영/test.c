#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main(void)
{
	int a;

	scanf("%d", &a);

	for (int i = 0; i < a; i++)
	{
		for (int j = a - i; j > 0; j--)
		{
			printf("*");
		}
		for (int k = 0; k < a; k++)
		{
			printf(" ");
		}
		printf("\n");
	}
	return 0;
}