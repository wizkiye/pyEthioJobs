from setuptools import setup, find_packages


def read_file(filename: str) -> str:
    with open(filename, encoding="utf-8", mode="r") as f:
        return f.read()


setup(
    name="pyEthioJobs",
    version="0.0.8",
    packages=find_packages(),
    url="https://github.com/wizkiye/pyEthioJobs",
    license="",
    author="Kidus",
    author_email="wizkiye@gmail.com",
    long_description=read_file("README.md"),
    install_requires=[
        "bs4",
        "httpx",
        "lxml",
    ],
    long_description_content_type="text/markdown",
    description="A python package to scrape jobs from ethiojobs.net",
)
