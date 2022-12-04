#include "lists.h"

/**
* is_palindrome - checks if a linked list is a palindrome
* @head: double pointer to head node of the singly linked list
* Return: 1 if list is a palindrome or 0 ortherwise
*/
int is_palindrome(listint_t **head)
{
	listint_t *tail;
	int *nums, *temp, i = 0, j = 0, half;

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
	temp = nums;
	while (tail)
	{
		*temp = tail->n;
		temp += 1;
		tail = tail->next;
	}
	half = i / 2;
	i--;
	for (j = 0; j < half; j++)
	{
		if (nums[j] != nums[i])
		{
			free(nums);
			return (0);
		}
		i--;
	}
	free(nums);
	return (1);
}
