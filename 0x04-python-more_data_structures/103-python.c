#include <Python.h>

void print_python_bytes(PyObject *p);

void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *element;

	size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		element = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);

		if (PyBytes_Check(element))
			print_python_bytes(element);
	}
}

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	printf("  first %ld bytes:", (size > 10) ? 10 : size);
	for (i = 0; i < 10 && i < size; i++)
	{
		printf(" %02x", (unsigned char)str[i]);
	}
	printf("\n");
}
