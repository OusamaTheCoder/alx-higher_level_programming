#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Print information about Python bytes objects
 * @p: PyObject bytes object
 */
void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes = (PyBytesObject *)p;
    Py_ssize_t i, size;

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", bytes->ob_base.ob_size);

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    printf("  trying string: %s\n", bytes->ob_sval);

    size = bytes->ob_base.ob_size < 10 ? bytes->ob_base.ob_size + 1 : 10;
    printf("  first %ld bytes: ", size);
    for (i = 0; i < size; ++i)
    {
        printf("%02x", (unsigned char)bytes->ob_sval[i]);
        if (i + 1 < size)
            printf(" ");
    }
    printf("\n");
}

/**
 * print_python_list - Print information about Python lists
 * @p: PyObject list object
 */
void print_python_list(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;
    Py_ssize_t i, size;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0, size = Py_SIZE(p); i < size; ++i)
    {
        printf("Element %ld: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
        if (PyBytes_Check(list->ob_item[i]))
            print_python_bytes(list->ob_item[i]);
    }
}

