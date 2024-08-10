[![Python package](https://github.com/saadshams/puremvc-python-multicore-framework/actions/workflows/python-package.yml/badge.svg)](https://github.com/saadshams/puremvc-python-multicore-framework/actions/workflows/python-package.yml)

# Installation

```commandline
pip install -r requirements.txt 
pip install PureMVC
```

## Documentation

```commandline
python3 setup.py sdist (bdist_wheel bdist_egg)
pip3 install dist/PureMVC-2.0.0.tar.gz

mkdir docs && cd docs && sphinx-quickstart (y)
cp ../build/conf.py ../build/index.rst source/
cd ../ && sphinx-apidoc -o ./docs/source/ ./src/puremvc
cd docs && make html && open build/html/index.html

# update documentation
python3 setup.py sdist && pip3 install dist/PureMVC-2.0.0.tar.gz
cd docs && make html && open build/html/index.html && cd ..
```

# Environment setup

1) pip install setuptools, pip install wheel
2) Applications > Python folder > double click on "Install Certificates.command" file
3) curl -sSL https://install.python-poetry.org | python3 -
4) export PATH="/Users/saad/.local/bin:$PATH" (source ~/.zshrc)
5) poetry env list
6) poetry init

## Reference

* [SetupTools](https://setuptools.pypa.io/en/latest/index.html)
* [PythonWheels](https://pythonwheels.com)
* [PythonEggs](http://peak.telecommunity.com/DevCenter/PythonEggs)
* [Classifiers](https://pypi.org/classifiers/)
* [Sphinx Documentation](https://www.sphinx-doc.org/en/master/index.html)
* [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html)

Creating your first PyPI package
https://www.youtube.com/watch?v=WGsMydFFPMk
