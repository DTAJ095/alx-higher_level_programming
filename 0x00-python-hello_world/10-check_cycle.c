#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has
 * a cycle in it
 * @list: the pointer to the list
 *
 * Return: 1 if there a cycle or 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	slow = fast = list;
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			list = fast;
			fast = slow;
			while (1)
			{
				slow = fast;
				while (slow->next != list && slow->next != fast)
				{
					slow = slow->next;
				}
				if (slow->next == list)
					break;
				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
