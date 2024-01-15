#include "main.h"
/**
* _strcat - combines two strings
* @dest: pointer
* @src: pointer
* Return: dest
*/
char *_strcat(char *dest, char *src)
{
	int x = 0;
	int y = 0;

	while (dest[x] != '\0')
	{
		x++;
	}
	while (src[x] != '\0')
	{
		dest[x] = src[y];
		x++;
		y++;
	}
	dest[x] = '\0';
	return (dest);
}

