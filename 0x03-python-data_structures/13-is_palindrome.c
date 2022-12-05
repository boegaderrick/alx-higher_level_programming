#include "lists.h"

/**
* add_nodeint - adds node at the beginning of linked list
* @head: pointer to pointer of address of first node
* @n: number to be held in new node
* Return: pointer to new node at start of list, NULL if operation failed
*/
void add_nodeint(listint_t **head, const int n)
{
	listint_t *ptr;

	ptr = malloc(sizeof(listint_t));
	ptr->n = n;
	ptr->next = *head;
	*head = ptr;
}

/**
* is_palindrome - checks if a linked list is a palindrome
* @head: double pointer to head node of the singly linked list
* Return: 1 if list is a palindrome or 0 ortherwise
*/
int is_palindrome(listint_t **head)
{
	listint_t *tail, *copy, *copy2;

	if (!head)
		return (1);
	tail = *head;
	copy = malloc(sizeof(listint_t));
	copy->n = tail->n;
	copy->next = NULL;
	while (tail)
	{
		add_nodeint(&copy, tail->n);
		tail = tail->next;
	}
	tail = *head;
	copy2 = copy;
	while (tail)
	{
		if (tail->n != copy->n)
		{
			free_listint(copy2);
			return (0);
		}
		tail = tail->next;
		copy = copy->next;
	}
	free_listint(copy2);
	return (1);
}
