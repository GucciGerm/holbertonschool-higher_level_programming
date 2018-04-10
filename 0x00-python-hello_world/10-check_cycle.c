#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Is a function that checks if a singly linked list has a cycle
 * @list: list is the linked list we will be checking
 *
 * Return: a 1 if there is a cycle or 0 if there is no cycle found
 */

int check_cycle(listint_t *list)
{
	listint_t *slowloop = list;
	listint_t *fastloop = list;

	while (slowloop && fastloop && fastloop->next)
	{
		slowloop = slowloop->next;
		/*we want our slowloop to go  to the next node*/
		fastloop = fastloop->next->next;
		/*we want our fastloop to go to the next next node*/
		if (slowloop == fastloop)
		{
			return(1); /* YAY A SUCCESS! CYCLE FOUND!! */
		}
	}
	return(0); /* No cycle found */
}
