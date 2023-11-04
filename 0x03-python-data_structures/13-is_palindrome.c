#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list
 * is a palindrome
 * @head: a pointer to the pointer to the head of the list
 *
 * Return: 1 if it's a palindrome or 0 if not
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL)
		return (0);

	return (check_palindrome(head, *head));
}

/**
 * check_palindrome - check if is palindrome
 * @left: the left
 * @right: the right
 *
 * Return: 1 if palindrome or 0 if not
 */

int check_palindrome(listint_t **left, listint_t *right)
{
	int boolean;

	if (right != NULL)
	{
		boolean = check_palindrome(left, right->next);
		if (boolean != 0)
		{
			boolean = (right->n == (*left)->n);
			*left = (*left)->next;
			return (boolean);
		}
		return (0);
	}
	return (1);
}
