#include "lists.h"

/**
 * insert_node - insert a number in a sorted singly linked list
 * @head: double poiter to the head of the list
 * @number: tne number to insert
 *
 * Return: the address of the new node or 0 if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	int flag = 0;
	listint_t *new_nd = NULL, *tmp = NULL, *next_ptr = NULL;

	if (head == NULL)
		return (NULL);
	new_nd = malloc(sizeof(listint_t));
	if (!new_nd)
		return (NULL);
	new_nd->n = number, new_nd->next = NULL;
	if (*head == NULL)
	{
		*head = new_nd;
		return (new_nd);
	}
	tmp = *head;
	if (number <= tmp->n)
	{
		new_nd->next = tmp, *head = new_nd;
		return (new_nd);
	}
	if (number > tmp->n && !tmp->next)
	{
		tmp->next = new_nd;
		return (new_nd);
	}
	next_ptr = tmp->next;
	while (tmp)
	{
		if (!next_ptr)
			tmp->next = new_nd, flag = 1;
		else if (next_ptr->n == number)
			tmp->next = new_nd, new_nd->next = next_ptr, flag = 1;
		else if (next_ptr->n > number && tmp->n < number)
			tmp->next = new_nd, new_nd->next = next_ptr, flag = 1;
		if (flag)
			break;
		next_ptr = next_ptr->next, tmp = tmp->next;
	}
	return (new_nd);
}
