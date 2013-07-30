LUMC Human Genetics programming course
======================================

This repository contains material for the first installment (August 2013) of
a programming course for scientists organised by the department of Human
Genetics of the Leiden University Medical Center.

See the [Trac Wiki](https://humgenprojects.lumc.nl/trac/programming-course)
for more information.


Software installation
---------------------

Todo (copy from our wiki).


Editing the slides
------------------

The slides are simple IPython notebooks, you can edit them by starting a
notebook server:

    ipython notebook

Choose `Slideshow` in the `Cell Toolbar` menu.

Some aditional information on editing slides in the Notebook can be found
here in [this presentation](http://www.slideviper.oquanta.info/tutorial/slideshow_tutorial_slides.html).


Live rendering of the slides
----------------------------

You can use nbconvert to convert the slides to HTML and serve them. For
example:

    ipython nbconvert --to slides --post serve numpy-slides.ipynb

This will open the slides in a new browser window.
