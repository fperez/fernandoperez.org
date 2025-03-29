# A hands-on 2-day Software Carpentry workshop at U. Hawaii

On November 30 and December 1 2012, we\'ll be holding a [Software
Carpentry Boot
Camp](http://software-carpentry.org/boot-camps/university-of-hawaii-november-2012/)
at U. Hawaii Manoa. This page contains the instructions on the tools you
need to set up in advance for the course.

We are hosting all [course
materials](https://github.com/swcarpentry/2012-11-uh) on github; [this
page](http://swcarpentry.github.com/2012-11-uh) has more details on the
schedule.

Please contact [Fernando](Fernando.Perez@berkeley.edu) or [Erik
Bray](embray@stsci.edu) if you run into any problems and we\'ll do our
best to assist you.

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

    sudo apt-get install git ipython python-scipy python-matplotlib python-nose

On Fedora or other non-apt distributions, please refer to your package
manager (the package names should be very similar).

## Test that everything is ready

Once you\'ve installed the code above, please download (save to your
disk) [this file](workshop_checklist.py) and execute it as per the
instructions contained in it (at the top). It runs a set of sanity
checks on your system to ensure that things are reasonably well
installed, and will provide diagnostics information along with
instructions on what to do.
