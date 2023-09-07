#!/usr/bin/env python
import sys
import platform
from setuptools import setup


def get_version():
    with open("pymorphy3/version.py", "rt") as f:
        return f.readline().split("=")[1].strip(' "\n')


# TODO: use environment markres instead of Python code in order to
# allow building proper wheels. Markers are not enabled right now because
# of setuptools/wheel incompatibilities and the 'pip >= 6.0' requirement.

# extras_require = {
#     'fast:platform_python_implementation==CPython': ["DAWG>=0.7.7"],
#     'fast:platform_python_implementation==CPython and python_version<3.5': [
#         "fastcache>=1.0.2"
#     ],
#     ':python_version<"3.0"': [
#         "backports.functools_lru_cache>=1.0.1",
#     ],
# }

is_cpython = platform.python_implementation() == 'CPython'
py_version = sys.version_info[:2]


install_requires = [
    'dawg-python >= 0.7.1',
    'docopt-ng >= 0.6',
    'pymorphy3-dicts-ru'
]
if py_version < (3, 0):
    install_requires.append("backports.functools_lru_cache >= 1.0.1")


extras_require = {'fast': []}
if is_cpython:
    extras_require['fast'].append("DAWG >= 0.8")
    if py_version < (3, 5):
        # lru_cache is optimized in Python 3.5
        extras_require['fast'].append("fastcache >= 1.0.2")


setup(
    name='pymorphy3',
    version=get_version(),
    author='Danylo Halaiko',
    author_email='d9nich@pm.me',
    url='https://github.com/no-plagiarism/pymorphy3',

    description='Morphological analyzer (POS tagger + inflection engine) for Russian language.',
    long_description=open('README.md').read(),

    license='MIT license',
    packages=[
        'pymorphy3',
        'pymorphy3.units',
        'pymorphy3.lang',
        'pymorphy3.lang.ru',
        'pymorphy3.lang.uk',
        'pymorphy3.opencorpora_dict',
    ],
    entry_points={
        'console_scripts': ['pymorphy = pymorphy3.cli:main']
    },
    install_requires=install_requires,
    extras_require=extras_require,
    zip_safe=False,

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Russian',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing :: Linguistic',
    ],
)
