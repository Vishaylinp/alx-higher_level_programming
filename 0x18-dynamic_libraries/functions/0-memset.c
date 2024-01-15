#include "main.h"
/**
* _memset - goes through memory and sets.
* @s: pointer
* @b: variable
* @n: number
* Return:s
*/
char *_memset(char *s, char b, unsigned int n)
{
	 unsigned int x = 0;

	while (x < n)
	{
		s[x] = b;
		x++;
	}
	return (s);
}
