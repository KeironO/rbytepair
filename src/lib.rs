use pyo3::prelude::*;
use pyo3::wrap_pyfunction;
use std::collections::HashMap;

#[pyfunction]
fn func_try() -> bool {
    return true;
}

#[pyfunction]
fn calculate_pair_statistics(vocab: Vec<String>) ->  PyResult<HashMap<String, i32>> {
   
    let mut map = HashMap::new();
    
    let _test = vocab.iter().map(|sequence| {
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
    }).collect::<Vec<_>>();
    

    Ok(map)
}

#[pymodule]
fn rnucpair(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(func_try))?;
    m.add_wrapped(wrap_pyfunction!(calculate_pair_statistics))?;
    Ok(())
}
