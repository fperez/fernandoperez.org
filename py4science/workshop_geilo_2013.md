# Installation instructions for Geilo Winter School

This page contains the instructions on the tools you need to set up in
advance for my lectures at the 2013 [Geilo Winter School on Reproducible
Science And Modern Scientific
Software](http://www.sintef.no/Projectweb/eVITA/Winter-Schools/2013).
Please [contact me](Fernando.Perez@berkeley.edu) if you run into any
problems and I\'ll do my best to assist you.

## Accounts and software install

Start by signing up for a (free) account on [Github](http://github.com).

**Mac or Windows users**

- Download and install [git](http://git-scm.com/downloads). You can
  accept all the default options from the installer.
- Download and install the free edition of the [Enthought Python
  Distribution (EPD)](https://www.enthought.com/products/epd_free.php).

You will also need to update the IPython notebook installation to the
current version:

- On a Mac, using the Terminal application:

      sudo enpkg enstaller
      sudo enpkg ipython

- On Windows, at the Command Prompt (`cmd.exe` application):

      enpkg enstaller
      enpkg ipython

**Linux users**

You can also use EPD, but most up to date distributions have everything
we need in their package managers. On Ubuntu or other Debian-based
distributions, type at the shell:

    sudo apt-get install ipython-notebook python-scipy python-matplotlib python-nose \
                         git gitk git-gui

On Fedora or other non-apt distributions, please refer to your package
manager (the package names should be very similar).

## Editing code

If you have a favorite programming editor already, skip this section.

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
- OSX: [Text Wrangler](http://www.barebones.com/products/textwrangler).
- Windows: [Notepad ++](http://notepad-plus-plus.org).

## Test that everything is ready

Once you\'ve installed the code above, please download (save to your
disk) [this file](workshop_checklist.py) and execute it as per the
instructions contained in it (at the top). It runs a set of sanity
checks on your system to ensure that things are reasonably well
installed, and will provide diagnostics information along with
instructions on what to do.
