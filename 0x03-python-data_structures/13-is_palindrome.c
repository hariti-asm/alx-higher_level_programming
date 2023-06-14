#include "lists.h"

/**
 * is_palindrome -> checks if a singly linked list is a palindrome
 * @head: Pointer Head
 * Return: Depend Condition
 */

int is_palindrome(listint_t **head)
{
	listint_t *is_slow = *head;
	listint_t *is_fast = *head;
	listint_t *prev = NULL;
	listint_t *temp;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (is_palindrome);
	while (is_fast != NULL && is_fast->next != NULL)
	{
		is_fast = is_fast->next->next;
		temp = is_slow;
		is_slow = is_slow->next;
		temp->next = prev;
		prev = temp;
	}
	if (is_fast != NULL)
		is_slow = is_slow->next;
	while (is_slow != NULL)
	{
		if (prev->n != is_slow->n)
		{
			is_palindrome = 0;
			break;
		}
		prev = prev->next;
		is_slow = is_slow->next;
	} temp = NULL;
	is_fast = prev;
	while (is_fast != NULL)
	{
		prev = is_fast->next;
		is_fast->next = temp;
		temp = is_fast;
		is_fast = prev;
	}
	*head = temp;
	return (is_palindrome);
}
