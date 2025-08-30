use pyo3::{prelude::*, types::PyList};
use std::fs;
use walkdir::WalkDir;


#[pyfunction]
fn glob(py: Python<'_>, path: String, recursive: Option<bool>) -> PyResult<&PyList> {
    let list: &PyList = PyList::empty(py);
    if recursive.unwrap_or(false) == false {
        for path in fs::read_dir(path).unwrap() {
            let _ = list.append(path.unwrap().path().display().to_string());
        }
    } else {
        for path in WalkDir::new(path) {
            let _ = list.append(path.unwrap().path().display().to_string());
        }
    };
    Ok(list)
}

#[pymodule]
fn rust_glob(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(glob, m)?)?;
    Ok(())
}
