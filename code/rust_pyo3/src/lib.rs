use pyo3::prelude::*;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn add(a: i32, b: i32) -> PyResult<i32> {
    Ok(a + b)
}

/// A Python module implemented in Rust.
#[pymodule]
fn simple_rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(add, m)?)?;
    Ok(())
}
