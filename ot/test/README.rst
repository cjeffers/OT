=============
Running tests
=============

The best way to run these tests is to use ``nose``, along with ``coverage``.
To install::

    $ pip install nose
    $ pip install coverage

To use::

    $ cd OT/ot/test
    $ ./test.sh

The output should look something like the following::

    ............................................................
    ............................................................
    .........
    Name             Stmts   Miss Branch BrMiss  Cover   Missing
    ------------------------------------------------------------
    ot                   0      0      0      0   100%
    ot.data             21      0      0      0   100%
    ot.dataset         169      0     46      0   100%
    ot.lattice          49      0     16      0   100%
    ot.ordertheory      68      0     36      0   100%
    ot.poot            156      0     50      0   100%
    ------------------------------------------------------------
    TOTAL              463      0    148      0   100%
    ------------------------------------------------------------
    Ran 129 tests in 19.691s

    OK

Use these tests if you're paranoid or to help you debug any additions you
make. On a clean install, the functions that try to load the lattice from
a pickle will fail, unless you generate the lattices (using either a script or
from the interpreter) and use::

    ot.lattice.PartialOrderLattice.write_to_pickle(dir)

where ``dir`` is set to ``OT/ot/lattices``
