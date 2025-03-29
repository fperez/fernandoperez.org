 (scicomp_course)=
# Modern Scientific Computing

An intensive course on the modern practice of scientific computing aimed
at the late-undergraduate or graduate level in the physical sciences,
mathematics and engineering.

## Introduction

Scientific computing, broadly understood as the use of computational
resources to solve research-specific problems, has in the last decade
grown immensely in its reach across disciplines as well as changing in
nature. The vast majority of computational effort in science during the
XXth century was devoted to the solution of numerical problems (first
exclusively with Fortran and then including other languages). But in the
past two decades, higher-level environments that allow for more rapid
and flexible development and incorporate extensive libraries, data
analysis and interactive exploration have become extremely popular. This
was pioneered by the creation of Matlab and IDL, followed by systems
with symbolic capabilities like Mathematica and Maple, all of them
commercial products.

Simultaneously, we reached the point where today, scientists from
virtually every discipline need to perform extensive computational work.
This is partly thanks to the existence of such systems that enable
someone who is not an expert at low-level programming to perform
sophisticated computational tasks, but also fueled by the explosion of
data that is flooding many fields in a way that inescapably mandates a
change towards semi-automated, large-scale computational analysis and
modeling (for a particularly interesting example of this, see [Josh
Bloom's](http://astro.berkeley.edu/~jbloom) current work on [automatic
real-time astronomical data acquisition and
analysis](http://128.150.4.107/awardsearch/showAward.do?AwardNumber=0941742))

In the last decade, open source alternatives to the above commercial
systems have emerged, and the most successful ones are all based on the
[Python](http://www.python.org) programming language, supported by a
vast array of additional tools and libraries to do everything from basic
array manipluation to sophisticated modeling and visualization.

This course will present a practical perspective on these tools, targeted at the level of graduate students in the physical sciences, mathematics and engineering. By practical we mean that we will not spend much time proving theorems regarding the convergence rate of a particular algorithm, for example. We *will* spend time discussing issues that sit at the intersection of scientific computing and software engineering, such as: documentation, testing and validation of codes, as well as version control and the participation of scientists as developers of their own research tools in open-source collaborations. This is important, because I have found through painful experience that often, scientific research projects have difficulties not because we aren't smart enough (we never are) or we don't work hard enough (we actually do put in a lot of time). The problems arise because of a nasty interlocking mess of poor *practices* regarding tool development, data management and accrual of verifyable results that leads to highly sub-optimal outcomes. This course will then try to at least touch on these topics as a natural part of the workflow. Rather than repeating here what others have said better I'd encourage you to look at Greg Wilson's excellent [Software Carpentry](http://software-carpentry.org) materials, as well as a related [post by Joel Spolsky](http://www.joelonsoftware.com/items/2009/10/26.html) which, despite being made in the context of a commercial software house, in my opinion applies 100% to our problem of interest. 

## Format

The course is organized around 24 hands-on 2-hour sessions, where we
will mix short presentations with work on actual problems to illustrate
and explore. The class will take place in a computer lab where systems
that have all the prerequisites pre-installed are available, but you are
also welcome to bring your own laptop if you so desire. I will present
short problems during class which you will be given some time to try and
solve, and whose solution we will then discuss immediately; longer
problems will be given as homework.

At the end of the course, a final project will be required of each
student, which can take one of two forms:

- A draft implementation of something of interest for one of your
  courses or research projects. I will be happy to discuss your problem
  and make suggestions on tools you can use as a starting point. You
  should plan on having something that does *run and produce some
  result* by the end of the course, even if it is preliminary in nature.
- A *working* improvement to any of the open-source tools we will be
  discussing and using in the course (ipython, numpy, scipy, matplotlib,
  mayavi, sympy, cython, sage, etc). You can fix an existing bug report,
  improve the documentation or implement a new feature. The choice of
  open-source project and specific task is yours, but I will expected
  you to actually produce the solution in the format expected by the
  project. This typically means joining its development mailing list,
  learning how to file the appropriate information in its bug tracking
  system and how to prepare your work for submission.

## Tools required

If you wish to install the tools in your own system, you can find the
necessary information in my [\"Starter
Kit\"](../py4science/starter_kit.html) page. It is important that you
actually *run* the [checklist
script](../py4science/workshop_checklist.py), which for example on my
Ubuntu 9.10 system produces:

    > python workshop_checklist.py 
    Running tests:
    __main__.test_imports('setuptools',) ... MOD: setuptools, version: 0.6c9
    ok
    __main__.test_imports('IPython',) ... MOD: IPython, version: 0.11.bzr.r1346
    ok
    __main__.test_imports('numpy',) ... MOD: numpy, version: 1.3.0
    ok
    __main__.test_imports('scipy',) ... MOD: scipy, version: 0.7.0
    ok

    [ lots of intermediate output removed ]

    Simple plot generation. ... ok
    Plots with math ... ok

    ----------------------------------------------------------------------
    Ran 21 tests in 37.571s

    OK

    ***************************************************************************
                   TESTS FINISHED
    ***************************************************************************

    If the printout above did not finish in 'OK' but instead says 'FAILED', copy
    and send the *entire* output (all info above and summary below) to the
    instructor for help.

    ==================
    System information
    ==================
    os.name      : posix
    os.uname     : ('Linux', 'maqroll', '2.6.31-17-generic', '#54-Ubuntu SMP Thu Dec 10 16:20:31 UTC 2009', 'i686')
    platform     : linux2
    platform+    : Linux-2.6.31-17-generic-i686-with-Ubuntu-9.10-karmic
    prefix       : /usr
    exec_prefix  : /usr
    executable   : /usr/bin/python
    version_info : (2, 6, 4, 'final', 0)
    version      : 2.6.4 (r264:75706, Dec  7 2009, 18:45:15) 
    [GCC 4.4.1]
    ==================

## Prerequisites

This course assumes the level of a graduate student in the physical
sciences, math or engineering, with a grasp of calculus, linear algebra,
ordinary differential equations, basic statistics and elmentary
numerical methods.

In addition, we will assume a *reasonable familiarity with programming*.
If you have never programmed in your life, I am afraid this is not the
course for you: I will not be teaching basic programming concepts from
scratch. Python is an extremely readable language, and its syntax is
regular and easy to remember, but this doesn't change the fact that
some ideas in programming require a certain amount of practice to
understand.

You must also *work through* (not just read, but actually type in and
execute) the basic [Python tutorial](http://docs.python.org/tutorial),
as well as the [introductory NumPy
tutorial](http://mentat.za.net/numpy/intro/intro.html). I will explain
Python syntax and language details as we go, but I will do so quickly;
it is therefore *really* important you have some practice with the
basics of the language and of Numpy arrays first.

Specifically, I assume you have read and understood these topics (you
don't have to be an expert, I will cover all of these, but they should
be reasonably familiar to you in general, and specifically in how Python
implements them):

- Basic types of the language (numbers, strings, lists, dictionaries)
- Function definition syntax
- Control flow primitives (if/else, for, while, break, continue)
- What an exception is, how to raise one and how to catch one
- How to define and instantiate a class
- How to open a text file on disk and read its contents
- How to write numbers to a text file on disk
- What a numpy array is and how it differs from a python list
- What basic operations a numpy array supports
- How to create a numpy array of uniform random numbers in a given
  interval

(hint: all of these are covered in the basic tutorials linked above).

Please see the [\"Starter Kit\"](../py4science/starter_kit.html) page
for detailed links to multiple references available online.

## Topics

The following is a *tentative* list of topics to be covered. I emphasize
tentative because I hope to adjust the actual workflow of the course
based on feedback from the students regarding background, interest and
relevance to your own projects.

- Introduction to the scientific [Python](http://www.python.org) stack
  of tools, and language review.
- Effective workflow techniques using [IPython](http://ipython.org).
- Introductory numerics with Python and [numpy](http://numpy.scipy.org).
- Numerical integration and root finding.
- Text processing.
- Dynamical systems, elementary chaos and error analysis.
- Elementary image processing with Numpy.
- Spectral techniques for image processing.
- Ordinary differential equations.
- Handling internet-based data: examples with financial datasets.
- Record arrays: sophisticated data management with Numpy.
- Statistics with Numpy and [Scipy](http://www.scipy.org).
- Data visualization with
  [matplotlib](http://matplotlib.sourceforge.net), in 2 and 3d.
- Data visualization with
  [Mayavi](http://code.enthought.com/projects/mayavi).
- Visually compelling 3d simulations with [VPython](http://vpython.org).
- Symbolic computing with [Sympy](http://code.google.com/p/sympy).
- Profiling and optimizing a program.
- Debugging techniques.
- Properly documenting your software.
- Writing codes you can believe in: automatic, reproducible testing.
- High-level distributed and parallel computing with IPython.
- f2py: interfacing with Fortran codes.
- scipy.weave: optimizing bottlenecks with C and C++.
- [Cython](http://cython.org): high-performance code with Python-like
  syntax.
- Introduction to [Sage](http://sagemath.org).
- Basics of software engineering: version control.
- Open source scientific computing: contributing to a project.
