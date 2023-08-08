#include "lists.h"

/**
 * check_cycle - checks if a list has a cycle
 * @list: linked list
 * Return: 1 if there's a cycle, 0 otherwise
*/

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
