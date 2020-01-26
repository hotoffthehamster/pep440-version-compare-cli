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

"""pep440cmp package tests."""

import pytest


class TestBasicRun(object):
    def test_basic_run(self, runner):
        """Make sure that invoking the command passes without exception."""
        result = runner()
        assert result.exit_code == 0


class TestVersionCompare(object):
    @pytest.mark.parametrize(
        ('ver1', 'oper', 'ver2', 'output', 'retcode'),
        [
            ('1.0.0', 'eq', '1.0.0', 'True\n', 0),
            ('1.0.1', 'ne', '1.0.1', 'False\n', 1),
            ('3.2.1a1', 'lt', '3.2.1', 'True\n', 0),
            ('9.9.9rc4', 'le', '9.9.9beta5', 'False\n', 1),
            ('15.333.4c5', 'ge', '15.333.4c4', 'True\n', 0),
            ('4.0.0', 'gt', '3.100.400', 'True\n', 0),
            # Result of comparing noise not defined, but
            # looks like pkg_resources treats weird vers.
            # like prerelease, e.g., this:
            ('@&sdf', 'lt', '3.2.1', 'True\n', 0),
        ],
    )
    def test_version_compare(self, runner, ver1, oper, ver2, output, retcode):
        """Ensure the 'test' command works as expected."""
        for be_explicit in (True, False):
            cli_args = ['test', ver1, oper, ver2]
            not be_explicit and cli_args.pop(0)
            result = runner(cli_args)
            assert result.stdout == output
            assert result.exit_code == retcode

    def test_version_bad_op_fail(self, runner):
        result = runner(['test', '1.2.3', 'xx', '6.6.6'])
        assert result.stdout.startswith('Usage: ')
        assert result.exit_code == 2


class TestIsPrerelease(object):
    @pytest.mark.parametrize(
        ('version', 'output', 'retcode'),
        [
            ('1.0.0', 'False\n', 1),
            ('1.0.0a1', 'True\n', 0),
        ],
    )
    def test_is_prerelease(self, runner, version, output, retcode):
        """Ensure the 'is-prerelease' command works as expected."""
        result = runner(['is-prerelease', version])
        assert result.stdout == output
        assert result.exit_code == retcode

