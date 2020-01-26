############
Installation
############

.. |virtualenv| replace:: ``virtualenv``
.. _virtualenv: https://virtualenv.pypa.io/en/latest/

.. |workon| replace:: ``workon``
.. _workon: https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html?highlight=workon#workon

To install system-wide, run as superuser::

    $ pip3 install pep440-version-compare-cli

To install user-local, simply run::

    $ pip3 install -U pep440-version-compare-cli

To install within a |virtualenv|_, try::

    $ mkvirtualenv pep440-version-compare-cli
    (pep440-version-compare-cli) $ pip install pep440-version-compare-cli

To develop on the project, link to the source files instead::

    (pep440-version-compare-cli) $ deactivate
    $ rmvirtualenv pep440-version-compare-cli
    $ git clone git@github.com:hotoffthehamster/pep440-version-compare-cli.git
    $ cd pep440-version-compare-cli
    $ mkvirtualenv -a $(pwd) --python=/usr/bin/python3.7 pep440-version-compare-cli
    (pep440-version-compare-cli) $ make develop

After creating the virtual environment,
to start developing from a fresh terminal, run |workon|_::

    $ workon pep440-version-compare-cli
    (pep440-version-compare-cli) $ ...

