Supported options
=================

The recipe supports the following options:

.. Note to recipe author!
   ----------------------
   For each option the recipe uses you should include a description
   about the purpose of the option, the format and semantics of the
   values it accepts, whether it is mandatory or optional and what the
   default value is if it is omitted.

option1
    Description for ``option1``...

option2
    Description for ``option2``...


Example usage
=============

.. Note to recipe author!
   ----------------------
   zc.buildout provides a nice testing environment which makes it
   relatively easy to write doctests that both demonstrate the use of
   the recipe and test it.
   You can find examples of recipe doctests from the PyPI, e.g.
   
     http://pypi.python.org/pypi/zc.recipe.egg

   The PyPI page for zc.buildout contains documentation about the test
   environment.

     http://pypi.python.org/pypi/zc.buildout#testing-support

   Below is a skeleton doctest that you can start with when building
   your own tests.

We'll start by creating a buildout that uses the recipe::

    >>> write('buildout.cfg',
    ... """
    ... [buildout]
    ... parts = buildperl
    ...
    ... [buildperl]
    ... recipe = pretaweb.recipe.perl
    ... url = http://www.cpan.org/src/perl-5.12.3.tar.gz
    ... """)

Running the buildout gives us::

    >>> print 'start', system(buildout) 
    start...
    Installing buildperl.
    ...

    >>> system("parts/perlbuild/bin/perl -e 'print \"Hello World\\n\";'")
    Hello World


