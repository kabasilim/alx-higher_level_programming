#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a node in a sorted singly linked list
 * @head: head node
 * @number: node to insert
 * Return: address of new node if successful or NULL otherwise
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *next_node, *new;

	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head ==  NULL)
	{
		*head = new;
		return (new);
	}
	current = *head;
	next_node = current->next;

	if (current->n > number)
	{
		new->next = current;
		*head = new;
	}
	else
	{
		while (next_node && current->n < number && next_node->n < number)
		{
			current = current->next;
			next_node = next_node->next;
		}
		new->next = current->next;
		current->next = new;
	}
	return (new);
}
