(code)=
# Software Tools

This page contains a collection of miscellaneous little software tools
that don't fit into any larger project but could be useful for someone.
Unless otherwise specified, they are all released under the terms of the
BSD license.

These days, I keep most new public projects available at my [github
repository](http://github.fperez.org), which makes for a convenient
download system and lets you send me back all the great improvements
you'll undoubtedly make.

## InDefero on Dreamhost

If you are interested in hosting your own projects privately using Git,
but with some facilities for project management (web interface to git,
source listings, issue tracking, etc), you may find [these
notes](indefero_dreamhost.html) on configuring the InDefero system on a
shared host useful.

(this_site)=
## How this site is built

:::{warning} No! This refers to my [old site!](https://fperez.github.io/fperez.org)

This one uses [MyST](https://mystmd.org).
:::

A number of people have asked me for the tools used to build this site,
so here is a brief description. The entire site is built using the
wonderful [Sphinx](http://sphinx.pocoo.org) toolset, with the addition
of a few custom scripts. For the impatient, you can download
[here](fperez.org.tgz) an archived export of most of the sources to this
site. After unpacking this, you can type:

    make

and you should be left with a semi-functional copy of my site in the
`_build/html` directory which you can see with a browser (note that some
links will be dead, since I removed most of the content to keep the
download small).

Then, edit the `conf.py` file and the `Makefile` to suit your needs.

Below are slightly more detailed instructions on what to do if this was
too terse for your taste.

:::{note}
If you use this material, please change the color schemes and other
details in the `themes/fperez` directory as well as the main images.
I've left them in place so things build out of the box, but I'd much
prefer it if your site did *not* have all the colors, layout and
pictures identical to mine.
:::

### Tools needed

Before getting started, make sure you have the following on your
computer, else nothing will really work:

- Make: standard on Linux, you may need to install XCode on OSX.
- [Python](http://www.python.org): Required for Sphinx and for my
  scripts to run.
- [Sphinx](http://sphinx.pocoo.org): The main documentation building
  tool.
- [ImageMagick](http://www.imagemagick.org): you only need this if you
  want to use my little thumbnail script (see below).
- Rsync: Standard on Linux and OSX, used to upload the site contents to
  a public location.
- [Firebug](http://getfirebug.com): pretty much needed to do *any* kind
  of debugging of web material.

### Workflow

These tools work with a very simple approach: the `conf.py` file
configures things for Sphinx, the `themes/fperez` directory contains the
layout and CSS necessary to render the site (this is configured in
`conf.py`), and the main Makefile has targets to build the files, update
the css for testing cosmetic changes, and to upload the final content to
a public site. The initial steps to get the system ready are:

1.  Edit `conf.py` to suit your taste.
2.  Please change the theme name and contents as requested above to your
    own.
3.  Edit the `Makefile` to indicate where you will upload the final site
    (the `WWW` variable). To make your life easier on uploads, I suggest
    you configure things for passwordless SSH key-based access, but
    that's up to you.

With these things ready, the normal workflow is:

1.  Edit files for content.
2.  To build the site, type:

<!-- -->

    make

3.  View the resulting site at `_build/html/index.html` in your browser.
4.  If you need to make changes to the CSS files only, type:

<!-- -->

    make css

for a quick update without needing a full rebuild.

5.  Occasionally if things don't look right, do a full cleanup/rebuild
    via:

<!-- -->

    make clean
    make

6.  Once you are happy with the results locally, push to your public
    site with:

<!-- -->

    make upload

### Additional details and Background reading

If you are interested in building a site with the same workflow, I
recommend that you first:

- Have a quick read of the official [Sphinx](http://sphinx.pocoo.org)
  documentation to get an idea of how things work. Don't go into too
  much detail, but knowing where the main ideas are described in the
  docs will save you time later.
- Do pay attention to the reST notes, because that's the syntax you'll
  be using to actually write. Note that on this site, I've left always
  visible the \"Show Source\" links on the right-hand navigation bar,
  which can be a useful way to learn how things are done. If you see
  anything in a page you are curious about, just click that link.
- Run through the very nice
  [Sampledoc](http://matplotlib.sourceforge.net/sampledoc) mini-tutorial
  written by John Hunter
  ([matplotlib](http://matplotlib.sourceforge.net)'s lead developer).
  That tutorial will get you 90% of the way there, and in fact you may
  find it sufficient for your purposes.

I personally needed a little bit on top of sampledoc; in particular I
wanted finer control over the layout of the site and decided to build a
full Sphinx theme (albeit a minimally modified one), and I also wanted
some tools to statically upload files like PDFs, zip archives or any
other content I might have in subdirectories into the public site. By
default sphinx does not upload non-reST files in any other directory
than its `_static` one, and I wanted to be able to populate arbitrarily
nested subdirectories with material like papers, talks or software
packages, and have those files uploaded *in the same location* to the
public site.

To achieve that, there's a simple script called
[copy_trees](../copy_trees.py) that copies my input trees to the Sphinx
output build directory prior to synchronization to the public site.

I also have written a tiny thumbnailer script, [mkthumb](../mkthumb)
that you may find useful to quickly create smaller images for inline
display. Note that this needs the `convert` utility from the
[ImageMagick](http://www.imagemagick.org) suite.

## Python tools for Mathematica and Fortran

With [Sage](http://sagemath.org) and
[Sympy](http://code.google.com/p/sympy), I have much less of a need for
Mathematica, but I've previously needed to easily transfer quantities
between Mathematica and Python. If you have similar needs, you may find
these tools useful (please drop me a line if you do).

- A Mathematica notebook, [math2python.nb](math2python.nb), defining
  functions to produce a Python module (meaning, valid, importable
  Python syntax) that contains variables from Mathematica. It will
  export all numbers as floats and (even nested) lists as numpy arrays.
- A Python module, [py2mathematica.py](py2mathematica.py) that does the
  opposite: it saves a list of Python variables to a valid Mathematica
  `.m` file, which can be loaded in Mathematica with the `<<fname`
  syntax. This module is fairly well documented.

I also have on occasion needed to produce static Fortran tables of
quantities computed elsewhere. Not so much from Python, but from
Mathematica, and it turned out to be much easier to use the above tools
to do the Mathematica -\> Python conversion, and then generate valid
Fortran from Python, than to convince Mathematica to do the job (its
string manipulation API, at least back in version 5.0, was hideous
beyond redemption). If you ever need to generate Fortran (77) from data
you have in Python, then [py2fortran.py](py2fortran.py) may come in
handy.

## X11 keyboard control

I recently modified and extended this [great little
script](http://www.larsen-b.com/Article/184.html) to control a keyboard
under X11. My use for it is to take advantage of the special keys in my
Microsoft Wireless keyboards under Linux, so I can control XMMS, call up
Mozilla, Konqueror, gthumb, etc.

It's a simple module which you can [find here](x11kbd.py), and I call
it via [this](mskbd) little script which you can modify for your
particular usage case. It should be very easy to customize it for any
keyboard and any behavior you want.

Note that you'll need the [Xlib
python](http://python-xlib.sourceforge.net) module.

## The attic: lyxport

Today, LyX has very robust PDF export (and probably also HTML). But that
wasn't the case in 2001, so I wrote this little tool in Perl called
[lyxport](lyxport/index.html) which managed to reliably produce valid
PDF and HTML out of lyx or tex sources better than LyX itself.

Today this code is probably of no interest, this is kept here mainly as
a curiosity and for archival purporses. But it was my first open source
tool that saw some widespread use, and I learned a lot writing it even
if the code looks awful today, even for the dubious standards of Perl
code.

::: {.toctree hidden=""}
indefero_dreamhost lyxport/index
:::
