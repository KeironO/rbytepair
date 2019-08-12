from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
    name="rbytepair",
    version="0.0.1",
    rust_extensions=[RustExtension("rbytepair.rbytepair", binding=Binding.PyO3)],
    packages=["rbytepair"],
    zip_safe=False,
)