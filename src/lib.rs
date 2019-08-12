use pyo3::prelude::*;
use pyo3::wrap_pyfunction;
use std::collections::HashMap;

#[pyfunction]
fn func_try() -> bool {
    return true;
}

#[pyfunction]
fn get_global_vocab(vocab: Vec<String>) -> PyResult<HashMap<String, i32>> {

}

#[pyfunction]
fn calculate_pair_stats(vocab: Vec<String>) ->  PyResult<HashMap<String, i32>> {
   
    let mut map = HashMap::new();
    
    for sequence in vocab.iter() {

        let inter = sequence.chars().collect::<Vec<char>>();

        for slice in inter.iter().collect::<Vec<_>>().windows(2) {
            
            let s: String = slice.iter().cloned().collect();
            
            match map.get_mut(&s) {
                Some(v) => *v += 1,
                None => ()
            }

            if !map.contains_key(&s) {
                map.insert(s, 1);
            }
        }
    } 

    Ok(map)
}

#[pymodule]
fn rnucpair(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(func_try))?;
    m.add_wrapped(wrap_pyfunction!(get_global_vocab))?;
    m.add_wrapped(wrap_pyfunction!(calculate_pair_stats))?;
    Ok(())
}
