##########################
pep440-version-compare-cli
##########################

.. image:: https://api.travis-ci.com/hotoffthehamster/pep440-version-compare-cli.svg?branch=develop
  :target: https://travis-ci.com/hotoffthehamster/pep440-version-compare-cli
  :alt: Build Status

.. image:: https://codecov.io/gh/hotoffthehamster/pep440-version-compare-cli/branch/develop/graph/badge.svg
  :target: https://codecov.io/gh/hotoffthehamster/pep440-version-compare-cli
  :alt: Coverage Status

.. image:: https://readthedocs.org/projects/pep440-version-compare-cli/badge/?version=latest
  :target: https://pep440-version-compare-cli.readthedocs.io/en/latest/
  :alt: Documentation Status

.. image:: https://img.shields.io/github/v/release/hotoffthehamster/pep440-version-compare-cli.svg?style=flat
  :target: https://github.com/hotoffthehamster/pep440-version-compare-cli/releases
  :alt: GitHub Release Status

.. image:: https://img.shields.io/pypi/v/pep440-version-compare-cli.svg
  :target: https://pypi.org/project/pep440-version-compare-cli/
  :alt: PyPI Release Status

.. image:: https://img.shields.io/github/license/hotoffthehamster/pep440-version-compare-cli.svg?style=flat
  :target: https://github.com/hotoffthehamster/pep440-version-compare-cli/blob/master/LICENSE
  :alt: License Status

A CLI wrapper around ``pkg_resources`` to compare versions using PEP 440 rules
(i.e., not SemVer rules).

This is especially important for comparing alpha versions when releasing to PyPI.

Usage

.. code-block:: bash

   $ pip install pep440-version-compare-cli

   $ pep440cmp 1.0.0 lt 2.0.0
   True
   $ echo $?
   0

   $ pep440cmp 1.0.0rc4 lt 1.0.0a5 > /dev/null
   $ echo $?
   1

