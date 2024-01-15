#include "main.h"
/**
* _memcpy - copies bytes from memory.
* @n: variable
* @dest: pointer
* @src: pointer
* Return: dest
*/
char *_memcpy(char *dest, char *src, unsigned int n)
{
	unsigned int x = 0;

	while (x < n)
	{
		dest[x] = src[x];
		x++;
	}
	return (dest);
}
