use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

#[pymodule]
fn rbytepair(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    Ok(())
}
