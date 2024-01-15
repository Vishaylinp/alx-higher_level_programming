#include "main.h"
/**
* _strchr - search string to find a character.
* @c: variable
* @s: pointer
* Return: s or null
*/
char *_strchr(char *s, char c)
{

	int x = 0;

	while (s[x] >= '\0')
	{
		if (s[x] == c)
		{
			return (&s[x]);
		}
		x++;
	}
	return (0);
}
