# PyMVPA - NiPy week

The authors of the [PyMVPA](http://www.pymvpa.org) Multivariate Pattern
Analysis toolkit will be visiting the UC Berkeley Brain Imaging Center
from April 14 until April 16 2009, to collaborate on the integration
between PyMVPA and [NiPy](http://neuroimaging.scipy.org).

As part of their visit, they will be presenting a two-part seminar on
multivariate pattern analysis. The first part is a general discussion on
the growing use of these techniques for data analysis in neuroscience,
and the second part is a more hands-on presentation of the pymvpa
project. We will take a short break between the two parts (at 11am) so
that you can attend only one of them if you need.

See below for details on these presentations, and do not hesitate to
contact me if you\'d like to schedule a technical discussion with
Michael and Yarick while they are visiting us.

## Speakers

- [Yaroslav O. Halchenko](http://www.onerussian.com/), Psychology
  Department, Rutgers-Newark
- [Michael
  Hanke](http://apsy.gse.uni-magdeburg.de/main/index.psp?page=hanke/main),
  Psychology Department, Magdeburg University

## Part 1: Reliable Decoding of Neural Data

- **When**: April 14 2009, 10 am
- **Where**: Tolman 5101

In the last five decades the number of techniques available for
non-invasive functional brain imaging has increased dramatically.
Researchers today can choose from a variety of neural data modalities
such as fMRI, EEG, MEG, etc. The peculiarities of each data acquisition
modality and the lack of strong interaction between the neuroscience
communities employing them have produced distinct analysis pipelines
specialized for the conventional analyses within a particular modality.
Some analysis techniques have become, due to normative concerns, de
facto standards despite their limitations and inappropriate assumptions
for the given data type (e.g. GLM in fMRI, ERP in EEG).

However, outside the neuroscience community, machine learning research
has spawned a set of analysis techniques that are typically generic,
flexible (e.g. classification, regression, clustering), powerful (e.g.
multivariate, linear and non-linear), and capable of efficient use of
both spatial and temporal evolutions of the signal.

Recently, neuroimaging researchers have begun to explore various
multivariate methods to address the shortcomings of the conventional
analysis approaches. Drawing on the field of statistical learning
theory, new analysis techniques possess explanatory power that could
provide new insights into the functional properties of the brain. By
constructing a decoder of neural data new analysis methods often reverse
the direction of the analysis and target the description of the behavior
or the environment in terms of the registered neural activity. Such
reversed paradigm can account for the covariance/causality structure
within the data and often allows for single-trial analysis of various
neural data modalities by decoding them into variables of interest.
Unbiased testing of the decoder on new samples of the data provides an
assessment of decoding performance validity. Furthermore, consecutive
analysis of the constructed decoder\'s sensitivity allows to identify
neural signal components relevant to the task of interest, hence
providing desired localization. These features make decoding approach
more powerful than conventional hypothesis-testing univariate methods
which currently dominate the neuroscience field.

This part of the PyMVPA-series would urge the necessity in developing
decoding methods of neural data analysis and will present already
published approaches and results.

## Part 2: PyMVPA: Fathom Brain Function with Multivariate Pattern Analysis

- **When**: April 14 2009, 11 am
- **Where**: Tolman 5101

Unlike the wealth of software packages for univariate analyses, there
are few packages that facilitate multivariate pattern classification
analyses of neural data. We offer a complete analysis framework to
exploit techniques from statistical learning theory for the reliable
analysis of neural data.

Here we introduce a Python-based, cross-platform, and open-source
software toolbox, called PyMVPA, for the application of statistical
learning methods toward the analysis of various neural data modalities.
PyMVPA makes use of Python\'s ability to access libraries written in a
large variety of programming languages and computing environments to
interface with the wealth of existing machine learning packages. In our
strong belief it is important not to limit the researcher in a single
analysis paradigm as it is often done by GUI-based toolkits formalizing
a specific analysis approach. Having that in mind, PyMVPA can be viewed
as a complete scripting environment which is capable not only of
replicating existing analysis methods, but also versatile enough to
implement a variety of custom analysis paradigms based on statistical
learning methods.

We will describe the PyMVPA framework: its building blocks and
convenience facilities. Furthermore we will provide illustrative
examples on its usage, features, and programmability.
