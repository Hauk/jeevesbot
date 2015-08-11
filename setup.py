from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import codecs
import os
import sys

import jeeves

here = os.path.abspath(os.path.dirname(__file__))

def read (*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.txt', 'CHANGES.txt')

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_test(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='jeeves',
    version=jeeves.__version__,
    url='http://github.com/Hauk/jeeves/',
    license='Apache Software License',
    author='Eoghan Lappin',
    tests_require=['pytest'],
    install_requires=[''],
    cmdclass={'test': PyTest},
    author_email='hauk@redbrick.dcu.ie',
    description='An IRC bot built for modularisation',
    long_description=long_description,
    packages=['jeeves'],
    include_package_data=True,
    platforms='any',
    test_suite='jeeves.test.test_jeeves',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 1 - Planning',
        'Natural Language :: English',
        'Environment :: Console :: Curses',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    extras_require={
        'testing': ['pytest'],
    }
)
