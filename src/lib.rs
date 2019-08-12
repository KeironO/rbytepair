use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

#[pyfunction]
fn func_try() -> bool {
    return true;
}

#[pymodule]
fn rbyte_pair(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(func_try))?;
    Ok(())
}
