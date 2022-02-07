import distutils.command.bdist_rpm as orig
from setuptools import SetuptoolsDeprecationWarning as SetuptoolsDeprecationWarning

class bdist_rpm(orig.bdist_rpm):
    def run(self) -> None: ...
