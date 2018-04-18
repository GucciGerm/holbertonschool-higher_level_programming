#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - Here we will check if a singly linked list is a palindrome
 * @head: is a pointer to the head of our linked list
 *
 *
 * Return: 0 if the output isnt a palindrome or 1 if there is a palindrome
 */

int is_palindrome(listint_t **head)
{
	/* First we want to take care of fail cases */
	if (*head == NULL || *head == NULL)
		return (1);
	return (check_palindrome(head, *head));
	/* return 0 because no palindrome found */
}
/**
 * check_palindrome - Here this function will check whether list is palindrome
 * @head: linked list
 * @end: end of our list
 *
 * Return: 0 if the output isnt a palindrome or 1 if there is a palindrome
 */

int check_palindrome(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (check_palindrome(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		/* if a palindrome was found */
		return (1);
	}
	/* if a palindrome was not found */
	return (0);
}
