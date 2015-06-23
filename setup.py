import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "orb",
    version = "0.0.1",
    author = "Josef Lange",
    author_email = "josef.d.lange@me.com",
    description = "Python client for CircleCI",
    license = "MIT",
    keywords = "circle ci circleci continuous integration testing building",
    url = "https://github.com/josefdlange/orb",
    packages = find_packages(),
    long_description = read('README.rst'),
    classifiers = [
        'Topic :: Utilities',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License'
        ]
)
