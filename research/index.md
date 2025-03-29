# Research

I come from a theoretical physics and applied mathematics background,
with a strong interest in building better tools for scientific
computing. Here is a brief description of topics I am {del}`currently`
interested in, with links to relevant publications.

:::{warning} This is actually old!!

These notes date back to ca. 2010; I'll update this soon.
:::

## Neuroscience and scientific computing

Briefly stated, today my work revolves at the intersection of
algorithmic development for neuroscience data analysis and scientific
computing. I am interested in mathematical methods that let us
understand the structure of brain function in a principled way from the
data we can acquire today non-invasively, and in the implementation of
these ideas with open-source, high-quality, well-documented and pleasant
to use computational tools.

The main technique we use at the U.C. Berkeley [Brain Imaging
Center](http://bic.berkeley.edu) is functional Magnetic Resonance
Imaging (fMRI), but I am in general more interested in the structure
that we can extract from the data that in the particular technique being
used, as I\'m convinced that we\'ll learn much more about the system by
combining multimodality data in a principled way.

I am collaborating with members of [Mark D\'Esposito\'s
lab](http://bic.berkeley.edu/despolab) on the analysis of several
different types of resting state data, and in the process we are
developing new software tools that will be made available as part of the
open-source [NiPy](http://nipy.sourceforge.net) project. I also
collaborate with [Michael Silver\'s
lab](http://argentum.ucbso.berkeley.edu), and currently [Ariel
Rokem](http://argentum.ucbso.berkeley.edu/ariel.html) is leading the
effort on the development of a library for the analysis of time-series
data. This is the [nitime](http://nipy.sourceforge.net/nitime) project,
another component of nipy. The following is a preprint of our recent
paper on this topic from the SciPy\'09 conference (you can also see the
[slides](http://conference.scipy.org/static/wiki/rokem_timeseries.pdf)
of Ariel\'s talk):

:::{admonition} Paper

A. Rokem, M. Trumpis, F. Pérez, [Nitime: time-series analysis for
neuroimaging data](../papers/nitime09_ro-tr-pe.pdf), Proceedings of the
8th Python in Science Conference (SciPy 2009).
[Bibtex](../papers/nitime09_ro-tr-pe.bib).
:::

These computational projects are part of my interest in the development
of modern, high-quality tools for scientific computing that take
advantage of the best practices from the open source revolution in
software development and bring them to computational research.

In the last couple of decades, but increasingly so in the last few
years, all scientific disciplines have been tossed into the deep end of
the computational pool, often while not being too well prepared for the
dip. Up until the end of the XX century, scientific computing was mostly
the domain of physicists, chemists and engineers. Fortran and C
dominated the scene, and for the most part scientific computing was
synonymous with high-end numerical analysis. But now, all disciplines
are drowning in quantitative data and need to develop a culture of
scientific computing. Fortunately the revolution in open source (made
possible by the opening of the Internet in the late 90\'s) has created a
lot of freely available tools, and a culture of how to use them and
develop them, that is causing lasting changes in scientific computing.

I believe that as discipline-focused scientists we have much to learn
from these developments, and I am trying to do my part in advancing the
state of the art on this problem, which I believe to be one of major
importance. Since late 2001, I have been actively involved in developing
tools of this kind based on the [Python](http://www.python.org)
programming language. I started the [IPython](http://ipython.org)
project to build an interactive environment I could use for my everyday
work, inspired by the tools I was accustomed to as a physicist,
especially Mathematica and IDL. I\'ve also contributed in various forms
to [NumPy](http://numpy.scipy.org), [SciPy](http://www.scipy.org),
[matplotlib](http://matplotlib.sourceforge.net) and
[Mayavi](http://code.enthought.com/projects/mayavi), all tools that
combined give us today an amazing array of computational functionality
based on the excellent qualities of Python as a programming language.
Here are two publications on this topic:

:::{admonition} Papers

F. Pérez, H-P. Langtangen and R. LeVeque, [Python for Scientific
Computing at CSE09](../papers/py4science09_siam_news.pdf), SIAM News,
42:5, 4 (2009). [Bibtex entry](../papers/py4science09_siam_news.bib).
(An [html version](http://www.siam.org/news/news.php?id=1595) is
available at the SIAM site).

F. Pérez and B. E. Granger. [IPython: a System for Interactive
Scientific Computing](../papers/ipython07_pe-gr_cise.pdf), Comput. Sci.
Eng. 9:3, 21-23 (2007).
:::

You can find [more details](/py4science) on the use of Python for
scientific computing and my work on this front.

(fast-algorithms)=
## New algorithms for PDEs and the Schrödinger equation

As a post-doc in the [Applied Mathematics](http://amath.colorado.edu)
department at the University of Colorado (Boulder) I worked with prof.
[Gregory Beylkin](http://amath.colorado.edu/faculty/beylkin) on the
development of novel algorithms for the solution of partial differential
equations (PDEs) in multiple dimensions. These methods use a
multiresolution approach to decompose functions and operators and a set
of approximations from the familiy of methods broadly referred to as
\"tensor decompositions\" that G. Belkyin developed in collaboration
with Lucas Monzón and prof. [Martin
Mohlenkamp](http://www.math.ohiou.edu/~mjm), to address the \"curse of
dimensionality\". In this formulation, PDE problems are handled in an
integral formulation (which has a number of advantages) since we now
have an efficient way of applying Green\'s functions.

The long-term goal of this effort is the development of accurate and
efficient methods to solve the many-electron Schrödinger equation, and
we made some theoretical and numerical progress on this front as well.

:::{admonition} Papers

G. Beylkin, M. J. Mohlenkamp and F. Pérez, [Approximating a Wavefunction
as an Unconstrained Sum of Slater
Determinants](../papers/freeslater08_be-mo-pe.pdf), Journal of
Mathematical Physics, 49, (2008).

G. Beylkin, V. Cheruvu and F. Pérez, [Fast adaptive algorithms in the
non-standard form for multidimensional
problems](../papers/nsform08_be-ch-pe.pdf), Applied and Computational
Harmonic Analysis, 24 (2008) 354\--377.

G. Beylkin, M. J. Mohlenkamp and F. Pérez, [Preliminary results on
approximating a wavefunction as an unconstrained sum of Slater
determinants](../papers/freeslater07_be-mo-pe.pdf), Proc. Appl. Math.
Mech., 7, (2007).
:::

## The attic

[My research attic](#attic) is an archive of projects I have worked on in the past and I am no longer actively pursuing. It turns out, however, that my current interest in the structure of neuroimaging datasets ties in closely with the problems in semi-classical chaos listed here, via questions on the highly excited eigenstates of the Laplacian operator. So I may end up returning to at least some of these topics that I actually hold very dear.
