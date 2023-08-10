#include "lists.h"
#include <stdio.h>
int check_cycle(listint_t *list)
{
	listint_t *urtle = list, *hares = list;
	int found = 0;

	while ((urtle && hares) && hares->next)
	{		
		urtle = urtle->next;

		if (hares->next || hares->next->next)	
			hares = hares->next->next;
		else
			break;

		if (urtle == hares)
		{
			found = 1;
			break;
		}
	}

	return (found);
}
