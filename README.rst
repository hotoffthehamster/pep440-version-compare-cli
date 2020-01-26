##########################
pep440-version-compare-cli
##########################

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

