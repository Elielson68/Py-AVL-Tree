import setuptools

with open("README.md") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Py-AVL-Tree",
    version="0.0.1",
    author="Elielson Barbosa",
    author_email="elielsonbr.com@gmail.com",
    description="A simple package to draw Binary Tree and balance the tree using AVL algorithm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)