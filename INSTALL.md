Software installation
=====================

The following guide gets you a virtual environment with all the necessary
packages installed.


Linux
-----

We assume Ubuntu (12.04 Quantal Quetzal or later) or Debian Linux (7.0 Wheezy
or later), but if you manage to install everything on a different flavour
that's also fine.

You can [download Ubuntu here](http://www.ubuntu.com/) and either install it
directly on your machine, or run it inside
[VirtualBox](https://www.virtualbox.org/).

Python version >= 2.7.3 and < 3.0 is required. This is installed by default on
Ubuntu and Debian Linux. Note that we use Python 2, *not* Python 3.

We need some system packages to be installed. For the following command, you
need sudo rights:

    sudo apt-get install -y \
      curl python-qt4 libfreetype6-dev libpng12-dev python-cairo \
      python-gtk2 python-gtk2-dev git gfortran

From here on, everything is local for the current user.

Install [virtualenv](http://www.virtualenv.org/) and
[virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/) using
[Virtualenv Burrito](https://github.com/brainsik/virtualenv-burrito):

    curl -sL https://raw.github.com/brainsik/virtualenv-burrito/master/virtualenv-burrito.sh | $SHELL
    source ~/.venvburrito/startup.sh

Automatically
[link PyGTK/Pycairo/PyQt system packages](https://gist.github.com/martijnvermaat/6111396/)
into our virtual environments:

    curl -sL https://gist.github.com/martijnvermaat/6111396/raw/postmkvirtualenv > ~/.virtualenvs/postmkvirtualenv

Create a virtual environment (named `programming-course`, but you could choose
any name here):

    mkvirtualenv programming-course

Install IPython:

    pip install ipython

Install some of the other package we'll use:

    pip install pyzmq tornado jinja2 pygments sphinx markdown nose
    pip install numpy
    pip install matplotlib
    pip install biopython

Define a default matplotlib backend:

    mkdir -p ~/.config/matplotlib
    echo "backend : GTKCairo" >> ~/.config/matplotlib/matplotlibrc


Mac OSX Mountain Lion
---------------------

Install
[Xcode from the App Store](https://itunes.apple.com/us/app/xcode/id497799835?ls=1&mt=12
Xcode from the App Store). Start Xcode and install the device support
(Preferences -> Downloads).

Install Xcode command line tools:

    ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"
    brew doctor
    xcodebuild -license   # accept license

Add user `bin`, and local Python to your `$PATH`:

    echo 'export PATH="~/bin:/usr/local/share/python:/usr/local/bin:$PATH"' > .bash_profile
    . .bash_profile

We need some system packages:

    brew install python --with-brewed-openssl
    brew install gfortran

Install [virtualenv](http://www.virtualenv.org/) and
[virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/) using
[Virtualenv Burrito](https://github.com/brainsik/virtualenv-burrito):

    curl -s https://raw.github.com/brainsik/virtualenv-burrito/master/virtualenv-burrito.sh | $SHELL
    source .venvburrito/startup.sh

Create a virtual environment (named `programming-course`, but you could choose
any name here):

    mkvirtualenv programming-course

Install IPython (version 1.0):

    pip install -e git+https://github.com/ipython/ipython#egg=ipython
    # or after its 1.0 release: pip install ipython

Install some of the other package we'll use:

    pip install pyzmq tornado jinja2 pygments sphinx markdown nose
    pip install numpy
    pip install matplotlib
    pip install biopython
