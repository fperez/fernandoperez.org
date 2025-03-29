# Python for scientific computing: a personal list of "warts"

While I don\'t hide the fact that I love Python for scientific computing
work, obviously no tool is perfect. I happen to think that Python is,
*today*, the best *compromise* we have available that combines the
following features:

- Open source, cross-platform and functional on a wide number of
  platforms, including supercomputers and other HPC environments.
- A high-level, very expressive language with readable syntax, a clean
  object model and useful built-in data types (strings, lists,
  dictionaries, sets, \...).
- A rich general-purpose library with support for common non-numerical
  tasks: networking, regular expressions and other text processing,
  database access, process management, operating system level tasks
  (file and directory manipulations), etc.
- A sophisticated array object for manipulating homogeneous collections
  of numerical data in a Fortran-like manner.
- A well-defined foreign function interface, and machinery to easily
  call existing codes in C, C++ and Fortran.
- A good body of bindings to common tools needed in scientific work: 2d
  and 3d plotting, numerical libraries, etc.
- Support for interactive work, including execution, visualization and
  debugging.
- Tools for documentation of code and automatic testing.

On any one of the above it\'s probably easy to find a better tool than
Python, but on the combination, I don\'t think that today we have any
better option. Perhaps in 10 years things will be different.

In the meantime, I\'ll focus on making Python as good of a tool as
possible for my own research, and one important aspect of working with a
tool you\'ve become used to, is not forgetting about its problems and
limitations. We often get so accustomed to the little (or big) problems
in the tools we use that we simply integrate workarounds into our mental
workflows, and stop being critical. This is the start of the
fossilization of a project, and I hope that doesn\'t happen to us on the
scientific python front. So I\'m trying to ask myself often about what
significant problems we still have in using Python efficiently every day
for scientific work, and occasionally third-parties also ask me this.

After a recent such discussion took place over email, I decided to make
this little page to track this question. This is meant to serve both as
a reminder to myself of these problems, and hopefully also as a list of
ideas for new contributors to jump in and help in areas that genuinely
require improvement. Please [email me](fernando.perez@berkeley.edu) with
corrections, ideas for working on any of this, or your own favorite
problem.

Off the top of my head, here are a few of Python\'s "warts" for
scientific work. Some of these are fixable, others are hurdles that only
impact the beginning user who comes from Matlab or IDL.

I should add that almost all of these are points that I often mention as
*advantages* of Python (e.g. incremental optimization). The solution to
the apparent contradiction is that I think we can still do much, much
better, and the fact that Python in some of these issues is better than
everything else that exists (not in all) should be no excuse to avoid
improving things.

Linear algebra syntax

:   For purely linear-algebra based problems, matlab\'s syntax can be
    cleaner than numpy\'s (multiplication, operator, array creation,
    etc).

Numpy ndarray is a complex object

:   Numpy\'s core object is the n-dimensional array, which is far more
    powerful than matlab\'s arrays, but can be more complex to master.

More complex core types in the language

:   Being a general language, it has multiple container types (sets,
    tuples, lists, n-dimensional arrays). This flexibility can be
    daunting for the beginner and intermediate user who sometimes
    misuses them, though it is a huge benefit for more advanced
    algorithmic development.

Lack of native rationals

:   I *really* wish Python had native rationals and that integer
    division produced rational results as needed. Python\'s native
    numerical types are pretty good for a general purpose language, as
    it includes out of the box arbitrary-length integers, floats,
    complex numbers (over the \'field\' of the floats) and even
    arbitrary-precision
    [decimals](http://docs.python.org/library/decimal.html). But the
    integers divide into the floats (they used to do integer truncating
    division, a la C). Since this is part of the very core of the
    language, no amount of GMP wrappers will make it easier (this is why
    [Sage](http://sagemath.org) has to preparse its input and convert
    input like `1+2` into `Integer(1)+Integer(2)`, so that all integer
    operations are done in a proper manner without burdening the user
    with that syntax all the time).

Array multiplication operator

:   I also wish that [PEP 225](http://www.python.org/dev/peps/pep-0225)
    or something like it were accepted, so that we could have at least a
    second multiplication operator to express constructs like matrix or
    vector products in addition to element-wise operations. See
    `this page <pep-225-discussion>`{.interpreted-text role="ref"} for
    background on this matter.

Packaging and distribution is a mess

:   The machinery for distributing python packages is brittle, buggy and
    generally a major pain to use and extend. There is currently
    (summer 2009) active work to address this; the core ideas are listed
    in Python\'s [PEP 376](http://www.python.org/dev/peps/pep-0376) and
    Tarek Ziadé (the person leading much of this effort) recently put up
    a [post on his
    blog](http://tarekziade.wordpress.com/2009/07/24/words-on-distribute-distutils-pep-376-pep-386-pep-345/)
    about it all.

Automatic testing

:   The automated testing systems for python are currently a bit
    fragmented. Python ships with two
    ([unittest](http://docs.python.org/library/unittest.html#module-unittest)
    and
    [doctest](http://docs.python.org/library/doctest.html#module-doctest))
    but these lack critical functionality and ease of use, which has led
    to third-party systems like
    [nose](http://somethingaboutorange.com/mrl/projects/nose), which
    isn\'t well integrated in the core. It would be great to see a merge
    of the good ideas of nose into the core in a robust and stable way.
    *Note*: progress is being made on this front for Python 2.7/3.2.

Growing pains with Python 3

:   The transition to Python 3 will cause some pain for a while, as the
    new version is not backwards compatible.

Integrated help and docs

:   There is no single-point-of-entry set of tools with unified
    documentation and help system for Python. The remarkable
    [Sage](http://sagemath.org) project does offer something like this
    and is an extremely valuable piece of this puzzle (I use it myself).
    Sage is a viable solution to this problem, though it actually goes
    beyond the pure python language by extending its syntax and
    modifying Python\'s core numerical type hierarchy. But in pure
    python, there is nothing that currently integrates execution,
    development, debugging and documentation with the polish of
    Mathematica or Matlab.

The infamous GIL

:   The main python implementation in C has a global lock (the GIL,
    short for Global Interpreter Lock) that prevents multithreaded code
    from modifying python data structures. So while python does support
    threads, they can only be used effectively for i/o bound tasks, not
    for cpu-bound ones. Google\'s [Unladen
    Swallow](http://code.google.com/p/unladen-swallow) project aims to
    correct this, but we\'ll have to wait a few more months to see if it
    succeeds. In the meantime, all parallel python code must use
    multiple processes, which can be a pain for certain valid use cases.

Very easy incremental optimization

:   There is currently no seamless way to get fast execution for
    numerical code that manually loops over arrays and does indexing
    operations on individual elements. In recent years, Matlab has
    developed JIT technology to support this, and currently no seamless
    equivalent exists for Python. Cython helps quite a bit on this
    front, but it\'s not yet 100% integrated into the system machinery
    (though rapid progress is being made).

Better docstrings in the standard library

:   For those of us who regularly work interactively, good docstrings
    make an enormous difference in the usability of a library. It is
    thus unfortunate that the quality of the docstrings in Python\'s
    standard library is so inconsistent (from very good to
    non-existent). Furthermore, I think we would all really benefit from
    having a standard for docstring formatting that included field
    descriptions for parametrs, return values, etc. In that view, I
    think the [numpy docstring
    standard](http://projects.scipy.org/numpy/wiki/CodingStyleGuidelines#docstring-standard)
    is in fact a very good starting point, as it does a good job of
    balancing readability in plain-text (important if you read the
    docstrings in source form) and expressiveness for postprocessing
    into HTML or PDF via sphinx.
