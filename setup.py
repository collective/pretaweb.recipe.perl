# -*- coding: utf-8 -*-
"""
This module contains the tool of pretaweb.recipe.perl
"""
import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '0.1'

long_description = (
    read('README.txt')
    + '\n' +
    'Detailed Documentation\n'
    '**********************\n'
    + '\n' +
    read('pretaweb', 'recipe', 'perl', 'README.txt')
    + '\n' +
    'Contributors\n'
    '************\n'
    + '\n' +
    read('CONTRIBUTORS.txt')
    + '\n' +
    'Change history\n'
    '**************\n'
    + '\n' +
    read('CHANGES.txt')
    + '\n' +
   'Download\n'
    '********\n')

entry_point = 'pretaweb.recipe.perl:Recipe'
entry_points = {"zc.buildout": ["default = %s" % entry_point]}

tests_require = ['zope.testing', 'zc.buildout',
    "hexagonit.recipe.cmmi",
    ]

setup(name='pretaweb.recipe.perl',
      version=version,
      description="Recipe which builds Perl and installs CPAM modules",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='',
      author='Adam Terrey',
      author_email='software@pretaweb.com',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['pretaweb', 'pretaweb.recipe'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'zc.buildout',
                        'hexagonit.recipe.cmmi',
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite='pretaweb.recipe.perl.tests.test_docs.test_suite',
      entry_points=entry_points,
      )
