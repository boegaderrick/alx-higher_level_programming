#include "lists.h"

/**
* insert_node - inserts node into sorted list
* @head: double pointer to head node of list
* @number: number to be stored in new node
* Return: address to new node or NULL of operation failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr, *new_node;

	new_node = malloc(sizeof(listint_t));
	new_node->n = number;
	new_node->next = NULL;
	ptr = *head;
	if (ptr == NULL)
	{
		*head = new_node;
		return (new_node);
	}
	while (ptr)
	{
		if (!ptr->next)
		{
			if (ptr->n < number)
				ptr->next = new_node;
			else
			{
				new_node->next = ptr;
				*head = new_node;
			}
			break;
		}
		if (ptr->n > number)
		{
			new_node->next = ptr;
			*head = new_node;
			break;
		}
		if ((ptr->n < number && ptr->next->n > number) || ptr->n == number)
		{
			new_node->next = ptr->next;
			ptr->next = new_node;
			break;
		}
		ptr = ptr->next;
	}
	return (new_node);
}
