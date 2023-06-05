#include "lists.h"

/**
 * check_cycle -> Check if Has cycle or not
 *
 * @list: Linked List
 *
 * Return: Depend Condition
*/

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL)
		return (0);
	slow = list;
	fast = list->next;
	while (fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
			return (1);

		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}
