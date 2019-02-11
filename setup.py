import sys

from setuptools.command.test import test as TestCommand
from setuptools import setup


class PyTest2(TestCommand):
    user_options = [("pytest-args=", "a", "")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ("")

    def run_tests(self):
        import shlex

        # import here, cause outside the eggs aren't loaded
        import pytest

        #command = ['/usr/bin/pylint']

        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)




setup(
    # ...,
    tests_require=["pytest"],
    cmdclass={"test": PyTest2},
)