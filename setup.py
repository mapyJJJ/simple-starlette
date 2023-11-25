import os
from setuptools import find_namespace_packages, setup

__version__ = "3.0.1"

find_file_path = (
    lambda file_name: os.path.split(__file__)[0] + "/" + file_name
)

requires = (
    open(os.path.join(os.getcwd(), "dev_requirements.txt"), "r")
    .read()
    .split("/n")
)
with open(
    os.path.join(os.getcwd(), "README.md"), "r", encoding="utf-8"
) as fh:
    long_description = fh.read()


setup(
    author="asbt",
    version=__version__,
    name="simple_starlette",
    packages=find_namespace_packages(),
    include_package_data=True,
    install_requires=requires,
    description="a micro server",
    author_email="sg5htd@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
