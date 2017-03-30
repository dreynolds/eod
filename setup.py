from distutils.core import setup

setup(
    name='EOD',
    version='0.1.0',
    author='David Reynolds',
    author_email='david@reynoldsfamily.org.uk',
    packages=['endofday', ],
    scripts=['bin/eod', ],
    license='LICENSE.txt',
    long_description=open('README.md').read(),
)
