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

"""Top-level package for this CLI-based application."""

import os
import sys

import click

from . import commands


class ClickCommandlessGroup(click.Group):
    """Override click.Group to let user run 'test' command implicitly."""

    def __init__(self, *args, **kwargs):
        """Wrap click.Group and keep track of whether current command is implicit."""
        super(ClickCommandlessGroup, self).__init__(*args, **kwargs)
        self.got_test_command = False

    def resolve_command(self, ctx, args):
        """Override parent method to replace arg to complete nameless command hack.

        Specifically, click.MultiCommand removes the first argument, assuming it's
        the command name -- but we might have overridden that logic in ``get_command``,
        in which case we need to undo the argument removal.
        """
        cmd_name, cmd, args_1_onward = super(
            ClickCommandlessGroup, self
        ).resolve_command(ctx, args)
        says_args = args_1_onward
        if self.got_test_command:
            says_args = args
        self.got_test_command = False
        return cmd_name, cmd, says_args

    def get_command(self, ctx, name):
        """Return the default test command if the user specifies no command name.

        That is, if the first argument is a version string, then get_command
        should return None, and we'll just assume the user wants to 'test'.
        """
        default_cmd = 'test'
        cmd = super(ClickCommandlessGroup, self).get_command(ctx, name)
        if cmd is None:
            # No command specified? No problem! Assume it's the compare command.
            cmd = super(ClickCommandlessGroup, self).get_command(ctx, default_cmd)
            self.got_test_command = True
        return cmd


@click.group(cls=ClickCommandlessGroup)
def cli():
    """Compares two versions, prints True or False, and exits 0 or 1.

    \b
    For example:

    \b
          $ pep440cmp 1.2.3 lt 1.2.4
          True
          $ echo $?
          0

    \b
          $ pep440cmp 4.5.6a1 ge 4.5.6
          False
          $ echo $?
          1
    """
    pass


cli.add_command(commands.pep440cmp.test)
cli.add_command(commands.is_prerelease.is_prerelease)

