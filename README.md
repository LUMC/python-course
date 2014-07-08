Programming course
==================

This repository contains material for the first installment (August 2013) of
a programming course for scientists organised by the department of Human
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


Slides
------

The top-level directory contains slides for the following lessons.

1. [Welcome](http://nbviewer.ipython.org/urls/raw.github.com/LUMC/programming-course/master/welcome.ipynb)
2. [Introduction to Python](http://nbviewer.ipython.org/urls/raw.github.com/LUMC/programming-course/master/python.ipynb)
3. [Version control with Git](http://nbviewer.ipython.org/urls/raw.github.com/LUMC/programming-course/master/git.ipynb)
4. [More Python Goodness](http://nbviewer.ipython.org/urls/raw.github.com/LUMC/programming-course/master/more-python.ipynb)
5. [Working with NumPy arrays](http://nbviewer.ipython.org/urls/raw.github.com/LUMC/programming-course/master/numpy.ipynb)
6. [Plotting with matplotlib](http://nbviewer.ipython.org/urls/raw.github.com/LUMC/programming-course/master/matplotlib.ipynb)
7. [Object-oriented programming](http://nbviewer.ipython.org/urls/raw.github.com/LUMC/programming-course/master/classes.ipynb)
8. [A sip of Biopython](http://nbviewer.ipython.org/urls/raw.github.com/LUMC/programming-course/master/biopython.ipynb)

Note: These links are to one-page renderings on [IPython Notebook Viewer](http://nbviewer.ipython.org/), see below how to get the real slideshows.


Editing the slides
------------------

The slides are simple IPython notebooks, you can edit them by starting a
notebook server:

    ipython notebook

Choose *Slideshow* in the *Cell Toolbar* menu.

Some aditional information on editing slides in the Notebook can be found
here in [this presentation](http://www.slideviper.oquanta.info/tutorial/slideshow_tutorial_slides.html).


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

    --RevealHelpTransformer.url_prefix=reveal.js

This would look for the reveal.js library in the `reveal.js` directory. A Git
submodule is already setup for this, so you can just do:

    git submodule init
    git submodule update

Also, if you just want to compile the slides to HTML without serving them to
your browser, leave out the `--post serve` argument.
