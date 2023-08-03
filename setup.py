from setuptools import setup, find_packages


def read_file(filename: str) -> str:
    with open(filename, encoding="utf-8", mode="r") as f:
        return f.read()


setup(
    name="pyEthioJobs",
    version="0.0.4",
    packages=find_packages(),
    url="https://github.com/wizkiye/pyEthioJobs",
    license="",
    author="Kidus",
    author_email="wizkiye@gmail.com",
    long_description=read_file("README.md"),
    install_requires=[
        "bs4>=0.0.1",
        "asyncio>=3.4.3",
        "weasyprint>=59.0",
        "httpx>=0.24.1",
        "lxml>=4.9.3",
    ],
    long_description_content_type="text/markdown",
    description="A python package to scrape jobs from ethiojobs.net",
)
