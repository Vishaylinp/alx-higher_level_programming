#include "main.h"
/**
* _strncat - combine two strings with a restriction.
* @dest: pointer
* @src: pointer
* @n: variable
* Return: dest
*/
char *_strncat(char *dest, char *src, int n)
{
	int x = 0;
	int y = 0;

	while (dest[x] != '\0')
	{
		x++;
	}
	while (src[y] != '\0' && n > 0)
	{
		dest[x] = src[y];
		x++;
		y++;
		n--;
	}
	dest[x] = '\0';
	return (dest);
}


