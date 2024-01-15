#include "main.h"
/**
* _strncpy - copy src into dest using a restriction
* @src: pointer
* @dest: pointer
* @n: var
* Return: dest
*/
char *_strncpy(char *dest, char *src, int n)
{
	int x = 0;
	int y = 0;

	while (src[y] != '\0' && x < n)
	{
		dest[x] = src[y];
		x++;
		y++;
	}
	while (n > x)
	{
	dest[x] = '\0';

	x++;
	}
	return (dest);
}
