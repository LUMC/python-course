LUMC Human Genetics programming course
======================================

This repository contains material for the first installment (August 2013) of
a programming course for scientists organised by the department of Human
Genetics of the Leiden University Medical Center.

See the [Trac Wiki](https://humgenprojects.lumc.nl/trac/programming-course)
for more information.


Introduction to Python
======================

Slides are created as an IPython Notebook (IPython 1.0) and exported to
reveal.js.


Installation in a virtual environment
-------------------------------------

Required IPython version is 1.0 and you can install it from source in a
virtual environment like this (on Debian Wheezy):

    mkvirtualenv --no-site-packages programming-course

We need IPython 1.0 which is not yet released, so we get it from GitHub:

    pip install -e git+https://github.com/ipython/ipython#egg=ipython

If IPython 1.0 is released, you can just do this:

    pip install ipython

Some additional packages:

    pip install pyzmq tornado jinja2 pygments sphinx markdown
    pip install numpy

For matplotlib, we need some development and system packages:

    sudo aptitude install libfreetype6-dev libpng12-dev python-cairo \
      python-gtk2 python-gtk2-dev
    mkdir -p $VIRTUAL_ENV/lib/python2.7/dist-packages
    ln -s /usr/lib/python2.7/dist-packages/{glib,gobject,gtk-2.0*,pygtk.pth} \
      $VIRTUAL_ENV/lib/python2.7/dist-packages/
    ln -s /usr/lib/pymodules/python2.7/cairo \
      $VIRTUAL_ENV/lib/python2.7/dist-packages/

    pip install matplotlib
    echo "backend : GTKCairo" >> ~/.matplotlib/matplotlibrc

If you want the IPython qtconsole to work, I found the following snippet to
take PyQT from system packages:

    https://gist.github.com/jlesquembre/2042882

We might want to use the same approach for the PyGTK/PyCAIRO stuff above.


Editing the slides
------------------

    ipython notebook python-intro.ipynb

Some aditional information on editing slides in the Notebook can be found
here:

http://www.slideviper.oquanta.info/tutorial/slideshow_tutorial_slides.html


Exporting the slides
--------------------

This will create a set of slides to be viewed in a browser:

    ipython nbconvert --FilesWriter.build_directory= --format reveal \
      python-intro.ipynb

As a reference for students, you could also create a full HTML dump:

    ipython nbconvert --FilesWriter.build_directory= --format full_html \
      python-intro.ipynb
