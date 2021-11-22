from setuptools import setup, find_packages

requires = [
    "starlette >= 0.16.0",
    "pydantic ~= 1.8.2",
    "werkzeug >= 2.0.2",
    "uvicorn[standard] == 0.15.0",
    "python_version >= '3.8.0'",
]


setup(
    name="simple_starlette",
    version="0.0.2",
    author="mapyJJJ",
    author_email="wszsdpyjjj@gmail.com",
    description=u"a micro server",
    install_requires=requires,
    packages=find_packages(),
)
