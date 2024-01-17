[![Python package](https://github.com/saadshams/puremvc-python-multicore-framework/actions/workflows/python-package.yml/badge.svg)](https://github.com/saadshams/puremvc-python-multicore-framework/actions/workflows/python-package.yml)

# Installation

```commandline
pip install -r requirements.txt 
pip install PureMVC
```

## Generate Documentation

```commandline
mkdir docs
cd docs && sphinx-quickstart
# COPY conf.py and index.rst
cd ../ && sphinx-apidoc -o docs puremvc
cd docs && make clean html

file:///Users/saad/Documents/puremvc/puremvc-python-multicore-framework/docs/build/html/index.html


sphinx-build -b html puremvc docs
make html
```