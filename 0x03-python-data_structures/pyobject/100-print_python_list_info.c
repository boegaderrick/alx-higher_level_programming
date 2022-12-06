#include <Python.h>
#include <listobject.h>
#include <object.h>

/**
* print_python_list_info - prints info about a python list
* @p: pointer to python object
*/
void print_python_list_info(PyObject *p)
{
	ssize_t i = 0;
	PyListObject *pyob = (PyListObject *)p;

	printf("[*] Size of the Python List = %zu\n", Py_SIZE(p));
	printf("[*] Allocated = %zu\n", ((PyListObject *)(p))->allocated);

	while (i < Py_SIZE(p))
	{
		printf("Element %zu: %s\n", i, Py_TYPE(pyob->ob_item[i])->tp_name);
		i++;
	}
}
