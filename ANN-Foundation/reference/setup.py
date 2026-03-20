from setuptools import setup, find_packages

setup(
    name="micrograd-plus",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib",
        "scikit-learn",
        "graphviz"
    ],
)