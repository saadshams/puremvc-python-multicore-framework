import pathlib

from setuptools import setup, find_packages

setup(
    name="PureMVC",
    version="2.0.0",
    description="PureMVC Multicore Framework for Python",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://puremvc.org",
    author="Saad Shams",
    author_email="saad.shams@puremvc.org",
    license="BSD License",
    project_urls={
        "Documentation": "",
        "Source": "https://github.com/PureMVC/puremvc-python-multicore-framework"
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Utilities"
    ],
    python_requires=">=3.9",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True
)
