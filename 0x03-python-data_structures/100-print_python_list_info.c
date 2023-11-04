#include <stdio.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Prints some basic info about Python lists
 * @p: object
 *
 * Return: Nothing
 */

void print_python_list_info(PyObject *p)
{
	long int list_size, allocate, i;

	i = 0;
	PyObject *object;

	list_size = PyList_Size(p);
	allocate = ((PyObject *p))->allocated;
	printf("[*] Size of Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", allocate);
	while (i < list_size)
	{
		object = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(object)->tp_name);
		i++;
	}
}
