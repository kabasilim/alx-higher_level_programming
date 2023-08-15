#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse - returns the reversed copy of a list
 * @head: pointer to the head node
 * Return: new head
*/
listint_t *reverse(listint_t *head)
{
	listint_t *new_head = NULL, *temp;

	if (head == NULL)
	{
		return (NULL);
	}
	while (head != NULL)
	{
		temp = (listint_t *) malloc(sizeof(listint_t));
		if (temp == NULL)
			return (NULL);
		temp->n = head->n;
		temp->next = new_head;
		new_head = temp;
		head = head->next;
	}
	return (new_head);
}
/**
 * is_palindrome - checks if a linked list is a palidrome
 * @head: pointer to the head node
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/

int is_palindrome(listint_t **head)
{
	listint_t *reverse_copy;

	if (*head == NULL)
		return (1);

	reverse_copy = reverse(*head);
	while (*head && reverse_copy)
	{
		if ((*head)->n != reverse_copy->n)
			return (0);
		*head = (*head)->next;
		reverse_copy = reverse_copy->next;
	}
	return (1);
}
