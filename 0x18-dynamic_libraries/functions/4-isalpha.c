#include "main.h"
/**
*  _isalpha - Print uppercase and lowercase
* @c: variable
* Return: (0)
*/
int _isalpha(int c)
{
	if (c >= 65 && c <= 122)
	{
		return (1);
	}
	else
	{
		return (0);
	}
}
