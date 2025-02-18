#!/usr/bin/env python
from setuptools import setup


def get_version():
    with open("pymorphy3/version.py", "rt") as f:
        return f.readline().split("=")[1].strip(' "\n')


install_requires = [
    'dawg2-python >= 0.8.0',
    'pymorphy3-dicts-ru',
    'setuptools >= 68.2.2 ; python_version >= "3.12"',
]


extras_require = {
    'CLI': ['click'],
    'fast': ['DAWG2 >= 0.9.0, < 1.0.0 ; platform_python_implementation == "CPython"']
}


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
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing :: Linguistic',
    ],
)
