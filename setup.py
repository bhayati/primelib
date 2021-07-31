from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="primelib-bhayati",
    version="0.0.1",
    author="Behzad Hayati",
    author_email="behzad.hayati@gmail.com",
    description="A small package to work with prime numbers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bhayati/",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
