#include "main.h"
/**
* _strcpy - copies string
* @src: pointer
* @dest: pointer
* Return: null terminator
*/
char *_strcpy(char *dest, char *src)
{
	int x;

	for (x = 0 ; src[x] != '\0'; x++)
	{
		dest[x] = src[x];
	}
return (dest);
}
