from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
    name="rnucpair",
    version="0.0.1",
    rust_extensions=[RustExtension("rnucpair.rnucpair", binding=Binding.PyO3)],
    packages=["rnucpair"],
    zip_safe=False,
)