#include "lists.h"

/**
 * list_reverse - function in C that checks
 * if a singly linked list is a palindrome
 * @head: pointer to the first node
 * Return: pointer to the new node first node
 */
void list_reverse(listint_t **head)
{
	listint_t *old = NULL;
	listint_t *curr = *head;
	listint_t *next = NULL;

	while (curr)
	{
		next = curr->next;
		curr->next = old;
		old = curr;
		curr = next;
	}

	*head = old;
}

/**
 * is_palindrome - frunction in C that checks if a
 * linked list is a palindrome
 * @head: double pointer to the linked list
 * Return: returns (1) if true and (0) if not
 */

int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head, *dub = NULL;
	listint_t *slow = *head, *fast = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dub = slow->next;
			break;
		}
		if (!fast->next)
		{
			dub = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	list_reverse(&dub);

	while (dub && tmp)
	{
		if (tmp->n == dub->n)
		{
			dub = dub->next;
			tmp = tmp->next;
		}
		else
			return (0);
	}

	if (!dub)
		return (1);

	return (0);
}
