#include "lists.h"

/**
* is_palindrome - checks if a linked list is a palindrome
* @head: double pointer to head node of the singly linked list
* Return: 1 if list is a palindrome or 0 ortherwise
*/
int is_palindrome(listint_t **head)
{
	listint_t *tail;
	int *nums, i = 0, j = 0, half;

	if (!head)
		return (1);
	tail = *head;
	while (tail)
	{
		i++;
		tail = tail->next;
	}
	nums = malloc(sizeof(int) * i);
	tail = *head;
	while (tail)
	{
		nums[j] = tail->n;
		j += 1;
		tail = tail->next;
	}
	half = i / 2;
	for (j = 0; j < half; j++)
	{
		i--;
		if (nums[j] != nums[i])
		{
			free(nums);
			return (0);
		}
	}
	free(nums);
	return (1);
}
