__version__ = "2.2.0"

from setuptools import find_packages, setup

requires = [
    "pyjwt==2.4.0",
    "pydantic~=1.8.2",
    "werkzeug>=2.0.2",
    "aiomysql>=0.0.21",
    "requests~=2.25.1",
    "starlette>=0.16.0",
    "SQLAlchemy>=1.4.27",
    "jsonrpcclient==4.0.1",
    "jsonrpcserver==5.0.4",
    "python_version>='3.8.0'",
    "uvicorn[standard]==0.15.0",
]

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    author="asbt",
    version=__version__,
    name="simple_starlette",
    packages=find_packages(),
    install_requires=requires,
    description="a micro server",
    author_email="sg5htd@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
