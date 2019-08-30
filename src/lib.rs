use pyo3::prelude::*;
use pyo3::wrap_pyfunction;
use pyo3::types::{PyDict};
use pyo3::exceptions::*;
use std::collections::HashMap;

#[pyfunction]
fn calc_global_vocab(vocab: Vec<String>) -> PyResult<HashMap<String, i32>> {
    let mut map = HashMap::new();

    for sequence in vocab.iter() {
        *map.entry(sequence.to_string()).or_insert(0) += 1;
    }

    Ok(map)
}

#[pyfunction]
fn calc_pair_stats(vocab: Vec<String>) -> PyResult<HashMap<String, i32>> {
    let mut map = HashMap::new();

    for sequence in vocab.iter() {
        let inter = sequence.chars().collect::<Vec<char>>();

        // IMPORTANT: Possible regression, non-ASCII data may mess all of this up.
        let last_two: String = inter[inter.len() - 2..].to_vec().iter().collect();
        let with_eol = format!("{}{}", last_two, "¿".to_string());

        for slice in inter.iter().collect::<Vec<_>>().windows(2) {
            let s: String = slice.iter().cloned().collect();
            *map.entry(s).or_insert(0) += 1;
        }

        *map.entry(last_two).or_insert(0) -= 1;

        *map.entry(with_eol).or_insert(0) += 1;
        // And in the case where a 0 is present (maybe the EOL was a specific pair
        // (regardless of however unlikely), we remove the adjacent key.
        map.retain(|_, v| *v != 0);
    }

    Ok(map)
}

#[pyfunction]
fn calc_num_symbols(py: Python, o: PyObject, num_symbols: usize, min_frequency: usize ) -> PyResult<PyObject> {

    if let Ok(d) = o.extract:: <&PyDict> (py) {
        Ok(d.items().to_object(py)) // get length of dictionary
    }
    else {
        Err(PyErr::new::<TypeError, _>("Unable to convert dictonary."))
    }

}

#[pymodule]
fn rnucpair(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(calc_global_vocab))?;
    m.add_wrapped(wrap_pyfunction!(calc_pair_stats))?;
    m.add_wrapped(wrap_pyfunction!(calc_num_symbols))?;

    Ok(())
}
