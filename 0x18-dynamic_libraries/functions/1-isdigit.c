#include "main.h"
/**
* _isdigit - identifies a digit.
* @c: variable
* Return: 0 and 1
*/
int _isdigit(int c)
{
	if (c >= 48 && c <= 57)
	{
		return (1);
	}
	else
		return (0);
}
