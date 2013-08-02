=============
Running tests
=============

The best way to run these tests is to use `nose`. To install::

    $ pip install nose

Then cd into the ot directory, and::

    $ nosetests

The output should look something like the following::

    ....
    ----------------------------------------------------------------------
    Ran 4 tests in 0.005s

    OK

This is the same output as Python's basic ``unittest`` module.

Use these tests if you're paranoid or to help you debug any additions you
make. If any tests fail on a clean install, reinstall, and if it still fails,
let the maintainer know.
