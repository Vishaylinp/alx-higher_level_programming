#include "main.h"
/**
* _strspn - counts the letters that are presented in both arrays
* @s: pointer
* @accept: pointer
* Return: c
*/
unsigned int _strspn(char *s, char *accept)
{
	unsigned int x = 0;

	while (*s != '\0' && *s == *accept)
	{
		x++;
		s++;
		accept++;
	}
	return (x);
}
