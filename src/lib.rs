use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

#[pyfunction]
fn func_try() -> bool {
    return true;
}

#[pyfunction]
fn calculate_pair_statistics(vocab: Vec<String>) ->  PyResult<(Vec<std::string::String>)> {
    Ok(vocab)
}

#[pymodule]
fn rnucpair(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(func_try))?;
    m.add_wrapped(wrap_pyfunction!(calculate_pair_statistics))?;
    Ok(())
}
