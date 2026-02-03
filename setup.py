import setuptools
from edgenextapisdk import version

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "edgenextapisdk",
    version=version,
    author="edgenextapisdk",
    author_email="edgenextapisdk@outlook.com",
    description="Api Sdk For Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/edgenextapisdk/edgenext-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        ##"Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
