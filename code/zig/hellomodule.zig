const py = @cImport({
    @cInclude("Python.h");
});

const PyObject = py.PyObject;
const PyMethodDef = py.PyMethodDef;
const PyModuleDef = py.PyModuleDef;
const PyModuleDef_Base = py.PyModuleDef_Base;
const Py_BuildValue = py.Py_BuildValue;
const PyModule_Create = py.PyModule_Create;
const METH_NOARGS = py.METH_NOARGS;

fn hello(self: [*c]PyObject, args: [*c]PyObject) callconv(.C) [*]PyObject {
    _ = self;
    _ = args;
    return Py_BuildValue("s", "Hello World from Zig :D");
}

var Methods = [_]PyMethodDef{
    PyMethodDef{
        .ml_name = "hello",
        .ml_meth = hello,
        .ml_flags = METH_NOARGS,
        .ml_doc = null,
    },
    PyMethodDef{
        .ml_name = null,
        .ml_meth = null,
        .ml_flags = 0,
        .ml_doc = null,
    },
};

var module = PyModuleDef{
    .m_base = PyModuleDef_Base{
        .ob_base = PyObject{
            .ob_refcnt = 1,
            .ob_type = null,
        },
        .m_init = null,
        .m_index = 0,
        .m_copy = null,
    },
    .m_name = "hellozig",
    .m_doc = null,
    .m_size = -1,
    .m_methods = &Methods,
    .m_slots = null,
    .m_traverse = null,
    .m_clear = null,
    .m_free = null,
};

pub export fn PyInit_hellozig() [*]PyObject {
    return PyModule_Create(&module);
}
