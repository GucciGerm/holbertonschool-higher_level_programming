#include <stdlib.h>
#include "lists.h" /* Standard definition */
#include <stdio.h>

/**
 * insert_node - This function will insert a # into a sorted linked list
 * @head: head will be the linked list we're referencing to
 * @number: number will just be the number we are inserting into our list
 *
 * Return: Null if it failed or the address of the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *currentnode;
	listint_t *newestnode; /* thought as list better as adding node */

	newestnode = malloc(sizeof(listint_t));
	if (!newestnode)
		return (NULL);

	/* malloc then place it in a structure! */
	newestnode->n = number;
	if (*head == NULL || (*head)->n >= newestnode->n)
	{
		newestnode->next = *head;
		*head = newestnode; /* new deref head points to newestnode */
	}
	else
	{
		currentnode = *head;
		while (currentnode->next != NULL && currentnode->next->n
		       < newestnode->n) /*while current is not equal to null */
			/* and */
			/*data being pointed from the next node to currentnode*/
			/*is less than the newestnode pointing to the next */
			/* execute within */
		{
			currentnode = currentnode->next;
		}
		newestnode->next = currentnode->next;
		currentnode->next = newestnode;
	}
	return (*head);
}
