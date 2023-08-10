#include "lists.h"
#include <stdlib.h>
listint_t *insert_node(listint_t **head, int num)
{
	listint_t *current = NULL, *new_node = NULL, *temp = NULL;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = num;
	if (*head)
	{
		current = *head;
		if (num <= current->n)
		{
			new_node->next = current;
			*head = new_node;
		}
		else
		{
			while (current->next)
			{
				if (num <= current->next->n)
				{
					temp = current->next;
					current->next = new_node;
					new_node->next = temp;
					return (*head);
				}
				current = current->next;
			}
			temp = current->next;
			current->next = new_node;
			new_node->next = temp;
		}
		return (*head);
	}
	new_node->next = NULL;
	*head = new_node;
	return (*head);
}
