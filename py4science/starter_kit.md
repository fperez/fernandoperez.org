(starter_kit)=
# Py4Science: a Starter Kit


:::{note}
Unfortunately, this page is woefully out of date and I currently have
very little time to keep it updated. Fortunately the quality of other
resources has greatly improved since I originally wrote it years ago, so
hopefully Google will be your friend this time around.
:::

This document is meant to gather resources for the scientist interested
in starting to use the Python programming language for scientific
computing. Most of the information here should be of general use, though
a few pointers are specific to resources at UC Berkeley. Please [email
me](Fernando.Perez@berkeley.edu) with feedback, corrections or
suggestions.

The landscape of Python tools for scientific computing is varied and
rapidly growing. Python wasn\'t originally designed specifically for
numerical computing but instead as a general purpose, high level
language. For this reason, as a scientist you will need to install some
extra tools on top of the basic language download to provide support for
array manipulations, numerical algorithms and data visualization. All of
the tools mentioned here are free and developed as open source software
in a collaborative manner by other scientists; I encourage you to not
only use these tools but to get involved with the groups that develop
them. You will find not only help with questions and problems, but
likely also the opportunity to shape the development of the major tools
in a way that improves them for your own research.

## What to download (the quick version)

Here are quick instructions on what to download to get started, especially if you will be soon attending a class or workshop I may be teaching. [At the end of this page](#download_long) there is a longer description of the various tools and distributions available, with some context to inform your decision.

For a basic verification that you have a functioning installation of the
core tools on your system, simply download and run [this checklist
script](workshop_checklist.py) as per the instructions at the top of the
file.

### On Linux

On a reasonably recent Linux distribution, all the tools you need are
available via the package management system. On Ubuntu or other
Debian-based distributions, type at the shell (tested on Ubuntu 9.10
Karmic):

    sudo apt-get install ipython ipython-notebook ipython-qtconsole \
      python-scipy python-matplotlib mayavi2 python-pandas \
      python-sympy cython python-networkx python-pexpect python-nose \
      python-setuptools python-sphinx python-pygments \
      python-tk build-essential

    sudo apt-get build-dep python python-scipy python-matplotlib mayavi2 cython

These two commands give you all the core packages to get started with
scientific Python work, including development tools like compilers. On
Fedora, the equivalent commands are (tested on Fedora 12):

    sudo yum install yum-utils

    sudo yum install python-ipython-notebook \
      scipy python-matplotlib Mayavi sympy Cython \
      python-networkx pexpect python-nose python-setuptools \
      python-sphinx python-pygments python-pandas

    sudo yum-builddep python scipy python-matplotlib Mayavi Cython

### On Mac OSX or Windows

Install the [Enthought Python
Distribution](http://www.enthought.com/products/epd.php) (I\'m assuming
here you are an academic user who can use the free license). This has
all of the above, and much more, in a single installer.

On the Mac, you will also want to have:

- The Apple [Xcode](http://developer.apple.com/technology/xcode.html)
  development toolkit. Once you register, it\'s a free (but fairly
  large) download.
- [The GNU Fortran compiler](http://r.research.att.com/tools).

### Editing code

Python is a programming language, so at some point you\'ll need to type
code. Learning how to use a good, powerful text editor is one of the
best investments of time you can make in terms of computing-related
skills. I\'m a life emacs user, but vi is equally sophisticated (in a
very different style). These editors, however, aren\'t the easiest to
get started with (if you\'re serious about computing though, I strongly
recommend you do learn how to use them).

If you want something with a slightly easier learning curve to begin
with, the following are all free, good options:

- Linux: gedit (typically installed by default).
- OSX: [Text Wrangler](http://www.barebones.com/products/TextWrangler),
  [TextMate (free for UC Berkeley
  affiliates)](http://software-central.berkeley.edu/software/92-TextMate)
- Windows: [Notepad
  ++](http://notepad-plus.sourceforge.net/uk/site.htm).

## What to read and view

### Online resources

As a starting point, I recommend that people at the very least *work
through* (not just read, but actually type in and execute) the basic
[Python tutorial](http://docs.python.org/tutorial), as well as the
[introductory NumPy
tutorial](http://mentat.za.net/numpy/intro/intro.html).

:::{note}
In all of these, the markers that you see as `>>>` are the prompts
generated by Python which you do not type. Similarly, the
[IPython](http://ipython.org) prompts look like `In [3]:`.
:::

In addition to these two minimal requirements, the following links can
also be useful:

- The NumPy [User Guide](http://docs.scipy.org/doc/numpy/user) and
  [Reference Guide](http://docs.scipy.org/doc/numpy/reference): these
  are works in progress but they contain much useful information.
- The [Matplotlib
  manual](http://matplotlib.sourceforge.net/contents.html): this is the
  Matlab-like plotting library most of us use regularly.
- The [IPython documentation](http://ipython.org/documentation.html):
  handy resources about making the most of your interactive environment.
- The [SciPy documentation
  page](http://www.scipy.org/Additional_Documentation) contains links to
  many more documentation resources, especially for scientific work.
- [Interactive data
  analysis](http://www.scipy.org/wikis/topical_software/Tutorial): a
  tutorial with an astronomy focus but very useful for anyone dealing
  with data. This is an *excellent resource* which you can download for
  reading but also with examples you can execute.
- [An introduction to Python and
  LaTeX](http://radiantbytes.com/books/python-latex): still (as of
  early 2010) a work in-progress, but already a useful introduction to
  Python programming targeted at students in science, math and
  engineering. This is part of the remarkable [FOSSEE
  India](http://fossee.in) project.

With a slightly broader view, I *very strongly* recommend you spend some
time with Greg Wilson\'s excellent [Software
Carpentry](http://software-carpentry.org) materials. As of early 2010 he
is restructuring them and I\'m sure the new version will be even better,
but even the archives have a lot of value; Greg addresses the real
problems that exist at the intersection of software engineering and
scientific computing and tries to offer not only practical solutions,
but more importantly, a set of approaches that hopefully lead to the
creation of a more robust computational culture in scientific work.

These are a few good links about how to write good Python code:

- Philip J. Guo\'s [Python
  idoms](http://www.stanford.edu/~pgbovine/python-idioms.htm).
- Rob Knight runs a stellar research group at CU Boulder, whose
  computational tools use Python heavily and has a great [collection of
  tips and idioms](http://jaynes.colorado.edu/PythonIdioms.html).
- David Goodger\'s [Code Like a Pythonista: Idiomatic
  Python](http://python.net/%7Egoodger/projects/pycon/2007/idiomatic/handout.html).

Quick reference: use [Richard Gruet\'s excellent Python Quick
Reference](http://rgruet.free.fr), available in html and pdf formats for
several Python versions.

At some point you\'ll need to debug your code, and [this
page](http://pythonconquerstheuniverse.wordpress.com/category/the-python-debugger/)
is the cleanest introduction to the Python debugger I\'ve read.

:::{note}
In IPython, you can run scripts under the control of the debugger by
typing `%run -d script.py`, and you can debug post-mortem by typing
`%debug` after any exception (or type `%pdb` to make this happen
automatically anytime there is an exception). The IPython debugger is an
extended version of the one described in this page, with syntax
highlighting and tab completion, but otherwise works identically.
:::

### Books

In terms of books for scientists, I recommend the following:

- [Python for Data
  Analysis](http://www.amazon.com/Python-Data-Analysis-Wrangling-IPython/dp/1449319793)
  by Wes McKinney: an excellent all-around data analysis book, with
  emphasis on understanding and using Pandas.
- [IPython Interactive Computing and Visualization
  Cookbook](http://ipython-books.github.io/cookbook/) and [Learning
  IPython for Interactive Computing and Data
  Visualization](http://ipython-books.github.io/minibook/) by Cyrille
  Rossant: both cover IPython and the surrounding scientific Python
  ecosystem, the latter being a short \"mini-book\" while the former is
  more comprehensive.
- [Beginning Python
  Visualization](http://www.apress.com/book/view/9781430218432) by Shai
  Vaingast: this is a great practical introduction to numerical data
  processing and visualization.
- [Python Scripting for Computational
  Science](http://folk.uio.no/hpl/scripting) by Hans Petter Langtangen:
  a longer and denser but very comprehensive discussion of using Python
  in scientific computing contexts, available online from the author
  ([Amazon
  link](http://www.amazon.com/Python-Scripting-Computational-Science-Engineering/dp/3540739157/ref=sr_1_1?ie=UTF8&s=books&qid=1248306847&sr=8-1)).
- [Matplotlib for Python
  Developers](http://www.packtpub.com/matplotlib-python-development/book)
  by Sandro Tosi: everything you need to know about producing meaningful
  and aesthetic data visualizations with Matplotlib.

The following Python books (except for David Beazley\'s) are freely
available to UC Berkeley via the O\'Reilly Safari system. These are
books I have personally found to be useful and can recommend; they are
general-purpose books without content specific to scientific use.

- [Learning Python, 3rd
  Edition](http://proquest.safaribooksonline.com/9780596513986) by Mark
  Lutz.
- [Python Pocket Reference, 2nd
  Edition](http://proquest.safaribooksonline.com/0596001894) by Mark
  Lutz.
- [Python in a Nutshell, 2nd
  Edition](http://proquest.safaribooksonline.com/0596100469) by Alex
  Martelli.
- [Python Cookbook, 2nd
  Edition](http://proquest.safaribooksonline.com/0596007973) by Alex
  Martelli; Anna Martelli Ravenscroft; David Ascher.
- [Python Essential Reference (4th
  Edition)](http://www.amazon.com/Python-Essential-Reference-David-Beazley/dp/0672329786/ref=sr_1_1?ie=UTF8&s=books&qid=1264128825&sr=1-1)
  by David M. Beazley. Not for the raw beginner, but if you have some
  programming experience, this is probably the most useful
  general-purpose Python book you can own.

:::{note}
U.C. Berkeley users can access Safari for free. For this you need to be
either on campus or browsing with the [Berkeley Library
Proxy](http://lib.berkeley.edu/Help/proxy.html).
:::

### Videos and webinars

In late 2008 I taught an intensive 2-day workshop introducing Python to
scientific users at UC Berkeley. While this was a very hands-on course
and thus probably not the best thing to watch as a recording, a number
of people have still told me that they find the lectures useful, all the
[video is
available](http://www.archive.org/search.php?query=Fernando+Perez+scientific+python).
They were kindly videotaped and put online by Jeff Teeters.

Enthought offers a [webinar
series](http://www.enthought.com/training/webinars.php) that is open to
the public, and recordings of past ones are available as well.

MIT\'s famous [6.00 Introduction to Computer Science and
Programming](http://ocw.mit.edu/OcwWeb/Electrical-Engineering-and-Computer-Science/6-00Fall-2008/CourseHome/index.htm)
course is now using Python and the whole course is available online on
their OpenCourseware system. In particular, [lecture
18](http://ocw.mit.edu/OcwWeb/Electrical-Engineering-and-Computer-Science/6-00Fall-2008/LectureVideos/detail/embed18.htm)
covers Matplotlib.

And there is a series of [basic Python tutorials on
YouTube](http://www.youtube.com/watch?v=4Mf0h3HphEA).

These are a few extra video lectures you may find useful:

**Scientific-computing oriented**

- SciPy 2009 conference: the entire tutorial series and conference
  [videos](http://www.archive.org/search.php?query=%22SciPy%202009%22)
  are online, as well as the
  [slides](http://conference.scipy.org/slides) for all presentations.
- [A Demonstration of the \'IPython\' Interactive
  Shell](http://video.google.com/videoplay?docid=3D2025411588241625522).
- [Matplotlib by John D.
  Hunter](http://videolectures.net/mloss08_hunter_mat/), a talk at
  NIPS\'08.
- [Scientific Computing with Python](http://nanohub.org/resources/99): a
  full day workshop presented by Eric Jones and Travis Oliphant, from
  [Enthought](http://www.enthought.com).
- Python for Scientific and High Performance Computing: a set of 4
  videos (several hours total) from a tutorial presented at the Chicago
  Python User\'s group, by folks from Argonne National Lab and other
  Chicago area institutions. [Part
  1](http://carlfk.blip.tv/file/2844247), [Part
  2](http://carlfk.blip.tv/file/2844521), [Part
  3](http://carlfk.blip.tv/file/2845210), [Part
  4](http://carlfk.blip.tv/file/2845400).
- [Sage](http://sagemath.org): Unifying Mathematical Software:
  [I](http://wstein.org/edu/2009/sd16/00021-stein-unifying_open_source_math_software-part1.m4v),
  [II](http://wstein.org/edu/2009/sd16/00022-stein-unifying_open_source_math_software-part2.m4v)

**General Python lectures**

- PyCon: [a selection from the annual Python
  conference](http://pycon.blip.tv):
  - Python 101: [I](http://blip.tv/file/1999483/),
    [II](http://blip.tv/file/1999358/).
  - Python 102: [I](http://blip.tv/file/1999205/),
    [II](http://blip.tv/file/1999063),
    [III](http://blip.tv/file/1998921).
  - Python 401: Some Advanced Topics:
    [I](http://www.blip.tv/file/2023288),
    [II](http://www.blip.tv/file/2023093),
    [III](http://www.blip.tv/file/2023307)
  - An Introduction to Object-Oriented Programming:
    [I](http://www.blip.tv/file/2022419/),
    [II](http://www.blip.tv/file/2022629/),
    [III](http://www.blip.tv/file/2022478/)
- [Advanced
  Python](http://video.google.com/videoplay?docid=3D7760178035196894549):
  a Google Tech Talk by Thomas Wouters.
- Google I/O 2008, \'Painless Python\':
  [I](http://www.youtube.com/watch?v=3DbDgD9whDfEY&feature=3Dchannel),
  [II](http://www.youtube.com/watch?v=3Dy7vwZ20SDzc&feature=3Dchannel).

## Where to get more help and information

All of the projects linked above have mailing lists that are very
welcoming; I have personally learned much from the discussions on these
lists. You will find that very knowledgeable people are surprisingly
generous with their time, if you ask questions carefully and provide
sufficient information to clearly delineate your problem. Simply click
on each project\'s main page and you will typically find an up-to-date
link to its mailing lists.

The [Planet SciPy](http://planet.scipy.org) blog aggregator is a useful
way to keep in touch with what many projects are doing.

Another excellent way to get in touch with what the developers of all
these tools are doing is to attend the annual SciPy
[conference](http://conference.scipy.org), which combines teaching
tutorials, formal presentations and development sprints.

If you are a UC Berkeley (or other Bay Area person for whom coming to
campus is feasible), I encourage you to stop by any of the regular
[Py4Science meetings on campus](https://wiki.ipython.org/Py4Science).
This informal group meets to discuss tools, problems and solutions
regarding the use of Python in scientific research; we have a very
low-traffic [mailing
list](https://calmail.berkeley.edu/manage/list/listinfo/py4science@lists.berkeley.edu)
for meeting announcements that anyone can subscribe to.

(download_long)=
## What to download (the longer version)

If you think of Python as a \'Matlab/IDL replacement\', you probably
want at the very least (before you download any of these individually,
continue reading below):

- A basic interactive environment: [IPython](http://ipython.org)
  (disclosure: I\'m biased since this is a project I started years ago,
  but many people seem to like it).
- Multidimensional array support: [NumPy](http://numpy.scipy.org) is the
  core library that most other scientific Python projects depend on and
  which allows it to efficiently manipulate large amounts of homogeneous
  numerical data in a manner similar to Matlab, IDL or any other array
  language.
- Linear algebra and other numerical libraries:
  [SciPy](http://www.scipy.org) is a set of libraries that add to NumPy
  access to all of LAPACK, FFTs, numerical integration, optimization,
  special functions, and much more. This is a large combination of old
  and well known codes in C and FORTRAN (many from
  [netlib](http://netlib.org)) with lots of new Python code both to
  expose those libraries and to provide new functionality.
- Data visualization: [Matplotlib](http://matplotlib.sourceforge.net) is
  my tool of choice for high quality 2d plotting (it recently also has
  developed basic 3d support), while
  [Mayavi](http://code.enthought.com/projects/mayavi) is a powerful
  system that builds on top of the [VTK](http://vtk.org) toolkit to
  provide sophisticated 3d visualization.

These are probably the raw basics, and a [community maintained
page](http://www.scipy.org/Topical_Software) at the SciPy site lists a
vast array of other tools you may find useful in your specific problem
domain, all of them free.

In terms of actually downloading and installing tools, there are a few
alternatives, partly depending on your operating system of choice:

- Linux: On most modern Linux distributions, the above tools (and many
  more) are one click or command away, though you might not get by
  default the very latest versions. As a starting point you will
  probably be fine.
- The [Enthought Python
  Distribution](http://www.enthought.com/products/epd.php) (EPD) is a
  self-contained installer with the above and many other tools. EPD is a
  very easy solution that is particularly appealing for Windows and Mac
  OSX, and it also exists for several Linux distributions and Solaris.
- [Python(x,y)](http://www.pythonxy.com) provides a single-click
  installer for Windows of a number of useful libraries, though
  unfortunately it does not ship the very useful Enthought tools (that
  include the powerful Mayavi 3d visualizer, the 2d plotting library
  Chaco and much more).

As an alternative approach, the [Sage](http://sagemath.org) project also
ships most of these tools, and then adds others (like GMP and Pari) to
provide a new numerical foundation, as well as its own original
libraries for many tasks. It also extends the Python language syntax and
modifies its core numerical type system with one based on more
structured mathematical abstractions (all integer arithmetic is
performed over the rationals, floating point numbers can always be
arbitrary precision ones, etc). Sage provides a web-based interactive
notebook environment (as well as a customized IPython command-line one)
but does not by default build the graphical user interface components
for Matplotlib and Mayavi. It\'s worth noting that since Sage has its
own numerical type system and matrix classes, by default most normal
numpy/scipy examples will not work in exactly the same way in Sage.
Depending on your needs, you can either use the Sage notebook in \'pure
python mode\' where it will not load Sage\'s native types, or use \'Sage
mode\' where its objects provide mathematical computing capabilities not
available in Python or NumPy.

Whether you choose to use the integrated Sage environment or the
individual libraries is up to you[^1]; I personally do most of my
development on top of \'bare\' Python using only the libraries I need
for each problem, but I always keep an updated Sage installation
available and use it as needed. Sage is available in source and binary
form for many different Unix-like operating systems, and can be used in
Windows as a VMWare Linux image.

## Acknowledgments

Thanks to Chris Burns from UC Berkeley for a useful set of links and
resources, to Stefan van der Walt from U. Stellenbosch for notes on Sage
and numerics, and to Gokhan Sever for a number of useful links.

---

[^1]: One point that may be of importance to you in making this decision, depending on your context, is licensing. Most of the tools I link to here are licensed in a [BSD](https://opensource.org/license/bsd-3-clause) or similar manner, except for Sage which is [GPL](https://opensource.org/licenses-old/gpl-license-html) licensed. Since Sage builds on a large foundation of other code that includes a mix of BSD and GPL tools, the combined Sage entity is necessarily also a GPL\'d project. 
