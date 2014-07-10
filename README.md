Programming course
==================

This repository contains material for the second installment (July 2014) of a
programming course for scientists organised by the department of Human
Genetics of the Leiden University Medical Center.

The course is targeted at PhD students, Postdocs, or anyone willing to learn
how to program in Python. Students are assumed to have some experience with
programming, but not necessarily in Python, and the UNIX shell.

The program consists of four mornings with lessons and some assignments to
be done in your own time (i.e., during the afternoons).

See the
[Trac Wiki](https://humgenprojects.lumc.nl/trac/humgenprojects/wiki/ProgrammingCourse)
for more information.


Software installation
---------------------

See the instructions in `INSTALL.md`.


Materials
---------

The top-level directory contains materials for the following lessons:

1. Welcome (slides) [view](http://nbviewer.ipython.org/urls/git.lumc.nl/humgen/programming-course/raw/master/welcome.ipynb)
2. Introduction to Python (slides) [view](http://nbviewer.ipython.org/urls/git.lumc.nl/humgen/programming-course/raw/master/python.ipynb)
3. More Python Goodness (notebook) [view](http://nbviewer.ipython.org/urls/git.lumc.nl/humgen/programming-course/raw/master/more-python.ipynb)
4. Working with NumPy arrays (slides) [view](http://nbviewer.ipython.org/urls/git.lumc.nl/humgen/programming-course/raw/master/numpy.ipynb)
5. Plotting with matplotlib (slides) [view](http://nbviewer.ipython.org/urls/git.lumc.nl/humgen/programming-course/raw/master/matplotlib.ipynb)
6. Object-oriented programming (slides) [view](http://nbviewer.ipython.org/urls/git.lumc.nl/humgen/programming-course/raw/master/classes.ipynb)
7. A sip of Biopython (notebook) [view](http://nbviewer.ipython.org/urls/git.lumc.nl/humgen/programming-course/raw/master/biopython.ipynb)

As indicated, some of the lessons are slideshows, whereas others are just
notebooks we scroll through during class. The links above are all one-page
static renderings on [IPython Notebook Viewer](http://nbviewer.ipython.org/).

We also have a
[repository with material for the assignments](https://git.lumc.nl/humgen/programming-course-assignments).


Notebooks
---------

We apply some custom styling to the notebooks (e.g., body width, font), which
is loaded in the last cell. This loads `styles/notebook.css` and
`styles/notebook.js`.

A variant `styles/notebook.css.small` is provided that is more suitable for
use on low-resolution displays. To use it, manually change the reference to
this file in the bottom cell, and rerun it.


Slideshows
----------

The sources for the slideshows are also IPython notebooks and you can edit
them by starting a notebook server:

    ipython notebook

Choose *Slideshow* in the *Cell Toolbar* menu.

Some aditional information on editing slides in the Notebook can be found
here in
[this presentation](http://www.slideviper.oquanta.info/tutorial/slideshow_tutorial_slides.html).

We also apply some custom styling to the slideshows, which is loaded in the
last cell.


Live rendering of the slides
----------------------------

You can use nbconvert to convert the slides to HTML and serve them. For
example:

    ipython nbconvert --to slides --post serve numpy.ipynb

This will open the slides in a new browser window. If you don't want that, add
this argument:

    --ServePostProcessor.open_in_browser=False

By default, the reveal.js library is loaded over the internet from a CDN. I
think it's usually not a good idea to rely on internet connectivity for your
slides, so you can also place a copy of reveal.js on your local computer and
specify the location like this:

    --reveal-prefix reveal.js

This would look for the reveal.js library in the `reveal.js` directory. A Git
submodule is already setup for this, so you can just do:

    git submodule init
    git submodule update

(Unfortunately, there are other online dependencies such Font Awesome, so
without an internet connection, not everything will look ok, but it will
work.)

Also, if you just want to compile the slides to HTML without serving them to
your browser, leave out the `--post serve` argument.
