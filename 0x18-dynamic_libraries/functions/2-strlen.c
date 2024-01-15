#include "main.h"
/**
* _strlen - count the number of characters in string.
* @s: pointer
* Return: the length of string
*/
int _strlen(char *s)
{
	int x;
	int y = 0;

	for (x = 0; s[x] != '\0'; x++)
	{
		y++;
	}
	return (y);
}
