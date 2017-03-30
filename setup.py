import os

from distutils.core import setup
from distutils.cmd import Command
from distutils.core import setup

here = os.path.abspath(os.path.dirname(__file__))


class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys, subprocess

        raise SystemExit(
            subprocess.call([sys.executable,
                             '-m',
                             'endofday.tests.test_eod']))

setup(
    name='EOD',
    version='0.1.0',
    author='David Reynolds',
    author_email='david@reynoldsfamily.org.uk',
    packages=['endofday', 'endofday.tests'],
    scripts=['bin/eod', ],
    license='LICENSE.txt',
    long_description=open(os.path.join(here, 'README.txt')).read(),
    cmdclass={
        'test': TestCommand,
    }
)
