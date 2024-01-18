from setuptools import setup, find_packages

setup(
    name="PureMVC",
    version="2.0.0",
    description="PureMVC Multicore Framework for Python",
    url="https://github.com/PureMVC/puremvc-python-multicore-framework",
    license="",
    author="Saad Shams",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    author_email="saad.shams@puremvc.org",
)
