#include "lists.h"

/**
* check_cycle - checks if a linked list has a cycle
* @list: pointer to linked list to be checked
* Return: 1 if cycle was found or 0 if otherwise
*/
int check_cycle(listint_t *list)
{
	listint_t *ptr, *ptr2;

	if (!list || !list->next)
		return (0);
	ptr = list;
	
	ptr2 = list;
	while (ptr)
	{
		while (ptr2)
		{
			if (ptr2 == ptr)
				return (1);
			ptr2 = ptr2->next;
		}
		ptr = ptr->next;
	}
	ptr = list;

	while (ptr)
	{
		ptr2 = ptr->next;
		while (ptr2)
		{
			if (ptr2 == ptr)
				return (1);
			ptr2 = ptr2->next;
		}
		ptr = ptr->next;
	}
	return (0);
}
