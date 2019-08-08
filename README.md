Programming course
==================

The course is targeted at PhD students, Postdocs, or anyone willing to learn
how to program in Python. Students are assumed to have some experience with
programming, but not necessarily in Python. In addition, they should bring
their own laptops for the practical sessions.

## Prerequisites

Affinity with the UNIX shell and git is required. For this reason it is
mandatory to follow our
[Practical Linux](https://git.lumc.nl/courses/practical-linux-course)
and [Code and data management with git](https://git.lumc.nl/courses/gitcourse)
courses before.

## Coordinates

- Date: TBA
- Time: TBA
- Location: TBA
- Teachers:
  - TBA
- Registration via www.medgencentre.com. Direct access to the [registration form](https://forms.lumc.nl/lumc2/PYTHONcourse).

Program and Materials
-------

- Mornings: presentations.
- Afternoons: assignments.

TBA

Assignments
-----------
TBA

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
