[![Python package](https://github.com/saadshams/puremvc-python-multicore-framework/actions/workflows/python-package.yml/badge.svg)](https://github.com/saadshams/puremvc-python-multicore-framework/actions/workflows/python-package.yml)

# Installation

```commandline
pip install -r requirements.txt 
pip install PureMVC
```

## Generate Documentation

```commandline
rm -r ../docs ../dist && cd ..

python3 setup.py sdist (bdist_wheel)
pip3 install dist/PureMVC-2.0.0.tar.gz

mkdir docs && cd docs && sphinx-quickstart (y)

cp ../build/conf.py ../build/index.rst source/

cd ../ && sphinx-apidoc -o ./docs/source/ ./src/puremvc

cd docs && make html && open build/html/index.html

python3 -c 'import site; print(site.getsitepackages())'
```

# Update Docs

```commandline
python3 setup.py sdist && pip3 install dist/PureMVC-2.0.0.tar.gz
cd docs && make html && open build/html/index.html && cd ..
```

# Environment setup

1) pip install setuptools, pip install wheel
2) Applications > Python folder > double click on "Install Certificates.command" file
2) curl -sSL https://install.python-poetry.org | python3 -
3) export PATH="/Users/saad/.local/bin:$PATH" (source ~/.zshrc)
3) poetry env list
4) poetry init

ls -alh /Library/Frameworks/Python.framework/Versions

poetry env use /Library/Frameworks/Python.framework/Versions/3.10/Python
poetry env use /Library/Frameworks/Python.framework/Versions/3.10/bin/python3.10
poetry env use /Library/Frameworks/Python.framework/Versions/3.12/bin/python3

ls -alh /Library/Frameworks/Python.framework/Versions/3.10
ls -alh /Library/Frameworks/Python.framework/Versions/3.10

## Reference

[SetupTools](https://setuptools.pypa.io/en/latest/index.html)
[PythonWheels](https://pythonwheels.com)
[PythonEggs](http://peak.telecommunity.com/DevCenter/PythonEggs)
[Classifiers](https://pypi.org/classifiers/)
[Sphinx Documentation](https://www.sphinx-doc.org/en/master/index.html)
[reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html)

Creating your first PyPI package
https://www.youtube.com/watch?v=WGsMydFFPMk
