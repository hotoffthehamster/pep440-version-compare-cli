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

"""A simple Click command to tell you if a version string is considered pre-release."""

import sys

import click
from pkg_resources import parse_version


@click.command()
@click.argument('version', nargs=1)
def is_prerelease(version):
    """If the passed version string is pre-release, prints 'True' and exits 0.

    Otherwise, if the version string is pre-release, prints 'False' and exits 1.
    """
    parsed = parse_version(version)
    result = parsed.is_prerelease
    print(str(result))
    sys.exit(not result and 1 or 0)

