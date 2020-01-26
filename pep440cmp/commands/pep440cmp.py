# This file exists within 'pep440-version-compare-cli':
#
#   https://github.com/hotoffthehamster/pep440-version-compare-cli
#
# Copyright © 2020 Landon Bouma. All rights reserved.
#
# Permission is hereby granted,  free of charge,  to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge,  publish,  distribute, sublicense,
# and/or  sell copies  of the Software,  and to permit persons  to whom the
# Software  is  furnished  to do so,  subject  to  the following conditions:
#
# The  above  copyright  notice  and  this  permission  notice  shall  be
# included  in  all  copies  or  substantial  portions  of  the  Software.
#
# THE  SOFTWARE  IS  PROVIDED  "AS IS",  WITHOUT  WARRANTY  OF ANY KIND,
# EXPRESS OR IMPLIED,  INCLUDING  BUT NOT LIMITED  TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE  FOR ANY
# CLAIM,  DAMAGES OR OTHER LIABILITY,  WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE,  ARISING FROM,  OUT OF  OR IN  CONNECTION WITH THE
# SOFTWARE   OR   THE   USE   OR   OTHER   DEALINGS  IN   THE  SOFTWARE.

"""A simple Click command to compare two version strings using ``pkg_resources``."""

import sys

import click
from pkg_resources import parse_version


def __compare_versions(versionl, comparison, versionr):
    """Return bool from results of PEP 440 version comparison.

    ... given two version strings and an comparison operator.
    """
    # - The code uses ``pkg_resources`` version implementation, which is 440-okay.
    #   I.e., the documentation for ``parse_version`` states::
    #     Parsed a project’s version string as defined by PEP 440.
    #   https://setuptools.readthedocs.io/en/latest/pkg_resources.html#parsing-utilities
    l_vers = parse_version(versionl)
    r_vers = parse_version(versionr)
    if comparison == 'eq':
        return l_vers == r_vers
    elif comparison == 'ne':
        return l_vers != r_vers
    elif comparison == 'lt':
        return l_vers < r_vers
    elif comparison == 'le':
        return l_vers <= r_vers
    elif comparison == 'ge':
        return l_vers >= r_vers
    elif comparison == 'gt':
        return l_vers > r_vers
    else:
        assert(False)


@click.command()
@click.argument('versionl', nargs=1)
@click.argument('comparison', type=click.Choice(['eq', 'ne', 'lt', 'le', 'ge', 'gt']))
@click.argument('versionr', nargs=1)
def test(versionl, comparison, versionr):
    """Compare versions. Prints 'True' or 'False', and exits 0 or 1, based on result.

    Specify two versions and an operator. If the statement is correct, the
    command prints 'True' to stdout and exits with a 0. If the statement is not
    true, the command prints 'False' to stdout and sets the exit status to 1.

    (So your code can either ignore stdout and look at the exit
    code, or it can ignore the exit code and look at the output.)

    Note that this command uses a PEP 440-compatible version comparison,
    which is not necessarily compatible with Semantic Versioning (SemVer).

    - For information on Python-style versioning, see:

      - PEP 440 -- Version Identification and Dependency Specification

        https://www.python.org/dev/peps/pep-0440/

    - For on SemVer and PEP 440-compatibility, see:

      https://semver.org/

      https://www.python.org/dev/peps/pep-0440/#semantic-versioning

    """
    result = __compare_versions(versionl, comparison, versionr)
    print(str(result))
    sys.exit(not result and 1 or 0)

