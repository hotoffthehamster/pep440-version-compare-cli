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

from pep440cmp import commands


# ***

# (lb): These are duplicated in setup.cfg:[metadata], but not sure how to DRY.
#   Fortunately, they're not likely to change.
__author__ = 'HotOffThe Hamster'
__author_email__ = 'hotoffthehamster+pep440cmp@gmail.com'
#
# (lb): Not sure if the package name is available at runtime. Seems kinda meta,
# anyway, like, Who am I? I just want to avoid hard coding this string in docs.
__package_name__ = 'pep440-version-compare-cli'
__arg0name__ = os.path.basename(sys.argv[0])


# ***

class ClickCommandlessGroup(click.Group):

    def __init__(self, *args, **kwargs):
        super(ClickCommandlessGroup, self).__init__(*args, **kwargs)
        self.got_test_command = False

    def resolve_command(self, ctx, args):
        """Replaces arg if click.MultiCommand removed because thought was command.

        The click.MultiCommand thinks the first arg is the command,
        so it removes it, e.g., returns `args[1:]`, which we undo if
        the user did not specify the command name and we just assumed.
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
        """Returns the default test command if user specifies no command name.

        (lb): I'll admit this is kinda hacky, but the broader question is, why am I
        bothering to use the Click library just to implement one command?
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
    pass


cli.add_command(commands.pep440cmp.test)
cli.add_command(commands.is_prerelease.is_prerelease)

