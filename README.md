Programming course
==================

The course is targeted at PhD students, Postdocs, or anyone willing to learn
how to program in Python. Students are assumed to have some experience with
programming, but not necessarily in Python, and the UNIX shell. In addition, 
they should bring their own laptops for the practical sessions.

## Coordinates

- Date: 27-30 November, 2017
- Time: 9:00 - 17:00
- Location: J1-83
- Teachers:
  - Sander Bollen
  - Jonathan Vis
  - Mark Santcroos
  - Guy Allard
  - Mihai Lefter
- Registration via www.medgencentre.nl. Direct access to the [registration form](https://forms.lumc.nl/lumc2/PYTHONcourse).

Program and Materials
-------

- Mornings: presentations.
- Afternoons: assignments.

| Day              | Time  | Lesson                              | Teacher  | 
|------------------|-------|------------------------------------ |----------|
| Tuesday, 27/11   | 9-10  | [Introduction][lesson_01_01] | Mihai    | 
|                  | 10-11 | [Data types][lesson_01_02]          | Mihai   |  
|                  | 11-12 | [Functions][lesson_01_03]          | Mihai    | 
|                  | 12-13 | Lunch break                      |          | 
|                  | 13-16 | Practical session | Mihai, Sander, and Guy|
| Wednesday, 28/11 | 9-10  | Assignments review                  |          |
|                  | 10-11 | [String methods, errors and exceptions][lesson_03_01]            | Mihai    | 
|                  | 11-12 | [Standard library, reading and writing files][lesson_03_02]            | Mihai    | 
|                  | 12-13 | Lunch break                      |          | 
|                  | 13-16 | Practical session | Mihai, Sander, and Mark|
| Thursday, 29/11  | 9-10  | Assignments review                  |          | 
|                  | 10-11 | [Object-oriented programming][lesson_oop]         | Jonathan | 
|                  | 11-12 | [Jupyter Notebook][lesson_jpn]       | Mark     |
|                  | 12-13 | [Data mangling with pandas][lesson_pandas]   | Mark     | 
|                  | 13-14 | Lunch break                      |          | 
|                  | 14-16 | Practical session | Mihai, and Mark|
| Friday, 30/11    | 9-10  | Assignments review                  |          | 
|                  | 10-11 | [Data visualisation with Matplotlib][lesson_dv_01] | Guy      |
|                  | 11-12 | [Data visualisation with Bokeh][lesson_dv_02]          | Guy      | 
|                  | 12-13 | [Biopython][lesson_bp]                          | Sander      | 
|                  | 13-14 | Lunch break                      |          | 
|                  | 14-16 | Practical session | Mihai, Sander, and Guy|

Some of the lessons are slideshows, whereas others are just
notebooks we scroll through during class. The links above are all one-page
static renderings on [IPython Notebook Viewer](http://nbviewer.ipython.org/).


Assignments
-----------
- [First day](https://classroom.github.com/a/QU2iPYKn).
- [Second day](https://classroom.github.com/a/UbifRH_y).
- Third day:
  - [OOP](https://classroom.github.com/a/8BnbL9fD).
  - [pandas](https://classroom.github.com/a/GOxWRQpa).
- Final day:
  - [Visualization 1](https://classroom.github.com/a/X7ElFXpu).
  - [Visualization 2](https://classroom.github.com/a/2GAOqqBu).


[lesson_01_01]: https://git.lumc.nl/courses/programming-course/raw/master/introduction/introduction/introduction.pdf?inline=false
[lesson_01_02]: https://git.lumc.nl/courses/programming-course/raw/master/introduction/data_types/data_types.pdf?inline=false
[lesson_01_03]: http://nbviewer.ipython.org/urls/git.lumc.nl/courses/programming-course/raw/master/introduction/02_introduction_to_python_3.ipynb
[lesson_03_01]: http://nbviewer.ipython.org/urls/git.lumc.nl/courses/programming-course/raw/master/more_python/03_more_python_goodness_1.ipynb
[lesson_03_02]: http://nbviewer.ipython.org/urls/git.lumc.nl/courses/programming-course/raw/master/more_python/03_more_python_goodness_2.ipynb
[lesson_oop]: https://git.lumc.nl/courses/programming-course/raw/master/oop/oop.pdf
[lesson_dv_01]: http://nbviewer.ipython.org/urls/git.lumc.nl/courses/programming-course/raw/master/visualization/DataVisualization1.ipynb 
[lesson_dv_02]: http://nbviewer.ipython.org/urls/git.lumc.nl/courses/programming-course/raw/master/visualization/DataVisualization2.ipynb 
[lesson_jpn]: http://nbviewer.ipython.org/urls/git.lumc.nl/courses/programming-course/raw/master/jupyter/05_jupyter.ipynb
[lesson_pandas]: http://nbviewer.ipython.org/urls/git.lumc.nl/courses/programming-course/raw/master/pandas/pandas.ipynb 
[lesson_bp]: http://nbviewer.ipython.org/urls/git.lumc.nl/courses/programming-course/raw/master/BioPython/Biopython.ipynb

Software installation
---------------------

See the instructions [here](https://docs.anaconda.com/anaconda/install/).

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

To serve on another IP address than the default 127.0.0.1, use the `ip`
configuration of the serve postprocessing. For example, to listen on all IP
addresses:

    --ServePostProcessor.ip=0.0.0.0

Changing the port can be done similarly with `port`.

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
