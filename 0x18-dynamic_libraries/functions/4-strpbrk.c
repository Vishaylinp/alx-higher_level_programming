#include "main.h"
/**
* _strpbrk - prints the character that is repeated.
* @s: pointer
* @accept: pointer
* Return: null and s
*/
char *_strpbrk(char *s, char *accept)
{
	int x;

	while (*s != '\0')
	{
		for (x = 0; accept[x] ; x++)
		{
			if (*s == accept[x])
			{
				return (s);
			}
		}
		s++;
	}
	return ('\0');
}
