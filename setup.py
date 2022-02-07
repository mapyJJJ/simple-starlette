__version__ = "1.0.0"

from setuptools import find_packages, setup

requires = [
    "starlette>=0.16.0",
    "pydantic~=1.8.2",
    "werkzeug>=2.0.2",
    "uvicorn[standard]==0.15.0",
    "python_version>='3.8.0'",
    "SQLAlchemy>=1.4.27",
    "aiomysql>=0.0.21",
    "jsonrpcclient==4.0.1",
    "jsonrpcserver==5.0.4",
    "requests~=2.25.1",
]


setup(
    name="simple_starlette",
    version=__version__,
    author="asbt",
    author_email="sg5htd@gmail.com",
    description=u"a micro server",
    install_requires=requires,
    packages=find_packages(),
)
