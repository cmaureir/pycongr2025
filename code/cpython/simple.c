#include <Python.h>

static PyObject* simple_hello(PyObject* self, PyObject* args){
    char *msg = "Hello from CPython!";
    return Py_BuildValue("s", msg);
}

static char simple_docs[] =
    "hello(): print hello message\n";

static PyMethodDef simple_funcs[] = {
    {"hello",                   // ml_name
     (PyCFunction)simple_hello, // ml_meth
     METH_NOARGS,               // ml_flags
     simple_docs},              // ml_doc
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef simplemodule = {
    .m_base = PyModuleDef_HEAD_INIT,
    .m_name = "simple",
    .m_size = 0,
    .m_methods = simple_funcs,
};

PyMODINIT_FUNC PyInit_simple(void){
    return PyModuleDef_Init(&simplemodule);
}
