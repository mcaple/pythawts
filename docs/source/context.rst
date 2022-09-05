===============
Python thoughts
===============

Version |version|


Context
=======

The idea of this documentation is to give myself an opportunity to create some documentation for a package that will attempt to give
clarity on how all my Python projects should be implemented. It is a collection of my current best practices along with some stuff I
find useful along the way. It is also the first time I have used Sphinx and it is always better to have something to do to learn a 
project.

Special mention should be given to `sphinx-from-scratch
<https://github.com/sadielbartholomew/sphinx-from-scratch>`_ for starting me on the Sphinx journey and
a lot of the links that I mention in :ref:`Quick links` are a direct copy of Sadie's work.


Install
-------

I will break the install up into a number of steps which combined allow a new project to be set up to be documented.

Initial
^^^^^^^

.. code-block:: console

    echo Only if not exists
    pip install sphinx

    mkdir python-thoughts 
    cd python-thoughts

    mkdir docs 
    cd docs

    sphinx-quickstart

.. note::

    | > *Separate source and build directories (y/n) [n]: y*
    | > *Project name: python-thoughts*
    | > *Author name(s): Mark Caple*
    | > *Project release []: 1.0*
    | > *Project language [en]:*

.. code-block:: console

    make html

    cd build/html
    npx http-server -p 9998

Now in a browser surf to http://localhost:9998

Useful extensions
^^^^^^^^^^^^^^^^^

Make following changes to docs/source/conf.py. 

.. code-block:: python

    ... replace the empty extensions list
    extensions = [
        "sphinx_rtd_theme",
        "sphinx.ext.autodoc",
        "sphinx.ext.autosummary",
        "sphinx_copybutton",
        "sphinx_toggleprompt",
        'sphinx.ext.autosectionlabel',
    ]

    ... replace the default html_theme
    html_theme = "sphinx_rtd_theme"

    ... at the end of the file paste
    # Generate _autosummary stub files as part of the build process
    autosummary_generate = True

    # Make sure the target is unique
    autosectionlabel_prefix_document = True

Package
^^^^^^^

As a lot of our time will be spent documenting packages that we produce, it makes
sense to create this documentation from a simplistic package called *pythawts*. We will 
create modules for each of the topics that we feel we need to give some thought and hence our package
will evolve. The first topic we shall discuss is the for loop and so we will create
here the initial content of that **core** module (by using core for all our module names we are in the position
of being able to split the topic of *for loops* into multiple modules) and will explain
how this module should be added to the package.

We will create a very simple package for our code documentation which will be based on
`build-your-first-python-package
<https://www.freecodecamp.org/news/build-your-first-python-package/>`_.

At the root of the project (1 up from docs folder)


.. code-block:: console

    mkdir pythawts
    cd pythawts
    touch __init__.py
    touch setup.py

    mkdir forthawts
    cd forthawts
    touch core.py


For each of the files copy the following content.

**setup.py**

.. code-block:: python

    from setuptools import setup

    setup(name='pythawts',
        version='1.0',
        description=(
            'A simple package that distills all my current'
            'beliefs on how Python should be written.'
        ),
        license='MIT',
    )    

**core.py**

.. code-block:: python

    """
    This module contains what I consider best practices for 'for loops'
    """

    def original_idea():
        """
        The description about original_idea
        """

        names = ["john", "jim", "mark"]

        for i in range(len(names)):
            print(names[i])

**__init__.py**

.. code-block:: python

    # Raise an error elegantly if the module fails to import:
    try:
        import pythawts
    except ImportError as err:
        raise ImportError(err)

    from .forthawts.core import *

Now we have created these files it is time to use our `autodoc
<https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_ (include documentation from docstrings) and 
`autosummary
<https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html>`_ (generates function/method/attribute summary lists) 
extensions to pull in the documentation automatically.

Create a file called api_reference.rst in docs/source and add the following. 

.. code-block:: rst

    Pythawts API
    ============

    .. currentmodule:: pythawts

    .. autosummary:\:
        :toctree: _autosummary

        forthawts.core

**At the time of writing I could not find a way of escaping the autosummary line above so you will need to delete the '\\' character
on the autosummary line after adding the content. If the autosummary was not done like this Sphinx would attempt to load autosummary
from within this context file which is not what is required.**

Now add a line containing api_reference directly under *context* in index.rst

When you now run 

.. code-block:: console

    make html

you will see the warning *"failed to import 'pythawts.forthawts.core': no module named pythawts.forthawts.core"*. To overcome
this we need to inform Sphinx where our code is. Go ahead and modify *conf.py* so that the path setup is as below. This will inform 
*autosummary* that our code is two directories up from where *index.rst* is found.

.. code-block:: console

    # -- Path setup --------------------------------------------------------------

    # If extensions (or modules to document with autodoc) are in another directory,
    # add these directories to sys.path here. If the directory is relative to the
    # documentation root, use os.path.abspath to make it absolute, like shown here.
    #
    import os
    import sys

    sys.path.insert(0, os.path.abspath("../.."))

As a final check to make sure you are setup switch to the root directory of python-thoughts and run a python interpreter pasting in 
the following 





.. code:: python

   from pythawts.forthawts.core import original_idea
   original_idea()

.. warning::
    If your interpreter is pre 3.9.2 then run

    .. code:: console

        echo "set enable-bracketed-paste off" >> ~/.inputrc

    in your console before running the interpreter, see `multiple line interpreter issue
    <https://www.linkedin.com/pulse/python-barfs-multiple-lines-fixed-daren-wilson>`_

Github
^^^^^^

We will be hosting this in github so we need a way to make this as painless as possible. Initially we will be following the 
procedure mentioned in `how-to-host-your-sphinx-documentation-on-github
<https://python.plainenglish.io/how-to-host-your-sphinx-documentation-on-github-550254f325ae>`_
but `docslikecode
<https://www.docslikecode.com/articles/github-pages-python-sphinx/>`_
is also useful.

The idea is that we will create a main branch for our full repository and a branch
called *gh-pages* which will be used as the source for the static pages for github.

-  Go to your github repository
-  Create a branch called *gh-pages*
-  Open the settings tab on the repository and select *Pages* from the sidebar
-  Select the branch *gh-pages*, folder */docs* and hit *Save*
-  Run ::

      git fetch origin

   to retrieve the *gh-pages* branch   
-  Create an empty file called *.nojekyll* in your docs folder (used to tell github to not do any styling) 
-  Create an html file in your docs folder called *index.html* with the following content
   ::

    <meta http-equiv="refresh" content="0; url=./html/index.html" />

   this allows us to redirect into the html folder that we will create below
-  Create an html folder in your docs folder called *html* 
   ::

      echo "We will create html in the gh-pages branch"
      git checkout gh-pages

      echo "Root directory"
      mkdir docs/html
      cp -a docs/build/html/. docs/html/.
      git add docs/html/.
      git commit -m "added initial html"
      git push origin

      echo "Leave the gh-pages branch"
      git checkout main



When complete we can view our documentation at https://mcaple.github.io/pythawts/

.. note::

    For further development, we may find it useful to style our documentation using the extension *sphinx.ext.githubpages* and a good example
    of how to do this can be found `here
    <https://gist.github.com/KCarretto/28d362210b41cfe28363fe8309ce5e6d>`_


.. _Quick links:

Quick links
===========

Examples of Sphinx-generated documentation
------------------------------------------


It is hard to tell what has been made with Sphinx without looking at the
codebase source, but often if you scroll to the bottom of some
documentation you can often see a "Created using Sphinx <sphinx version>"
note in the footer. A small number of examples are referenced below.

* A large but absolutely not comprehensive listing collected by the Sphinx
  team: https://www.sphinx-doc.org/en/master/examples.html
* Sphinx's own documentation (made with Sphinx, of course!):
  https://www.sphinx-doc.org/en/master/
* Python 3 documentation: https://docs.python.org/3/
* Python 2 documentation: https://docs.python.org/3/
* Tornado documentation: https://www.tornadoweb.org/en/stable/
* Official RST documentation (note it is also made in Sphinx):
  https://docutils.readthedocs.io/en/sphinx-docs/user/rst/quickstart.html
* Dask documentation: https://docs.dask.org/en/latest/
* JupyterHub documentation: https://jupyterhub.readthedocs.io/en/stable/
* NumPy documentation: https://numpy.org/doc/stable/reference/
* A small (slightly old) listing of non-Python projects with Sphinx
  documentation:
  https://ericholscher.com/blog/2014/feb/11/sphinx-isnt-just-for-python/
* An example of a book made with Sphinx: https://www.theoretical-physics.net/


Sphinx
------

Basic
^^^^^


* Sphinx documentation homepage: https://www.sphinx-doc.org/en/master/
* Quick start including `sphinx-quickstart` command:
  https://www.sphinx-doc.org/en/master/usage/quickstart.html
* HTML themes: https://www.sphinx-doc.org/en/master/usage/theming.html
  
Advanced
^^^^^^^^

* Guidance on extensions:
  https://www.sphinx-doc.org/en/master/usage/extensions/index.html
* An "awesome" listing of extra Sphinx resources:
  https://github.com/yoloseem/awesome-sphinxdoc
* Big listing of even more HTML themes: https://sphinx-themes.org/
* Our customisation of the "alabaster" default theme, in practice:
  https://ncas-cms.github.io/cf-python/
* Example Sphinx extension project repositories:

  * ``sphinx-copybutton`` (button to copy code in code examples):
    https://github.com/executablebooks/sphinx-copybutton 
  * ``sphinx-toggleprompt`` (button to hide prompts and outputs in
    console-like code examples):
    https://github.com/jurasofish/sphinx-toggleprompt
  * ``sphinx-pyreverse`` (generates UML diagramms of the code or parts of
    it into the documentation): https://github.com/alendit/sphinx-pyreverse


reStructuredText (`.rst` extension) format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Official reStructuredText documentation (note it is also made in Sphinx):
  https://docutils.readthedocs.io/en/sphinx-docs/user/rst/quickstart.html
* Helpful cheatseets:

  * https://docutils.sourceforge.io/docs/user/rst/quickref.html
  * https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst


Documenting projects with Sphinx
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* A nice blog post: https://medium.com/@richdayandnight/a-simple-tutorial-on-how-to-document-your-python-project-using-sphinx-and-rinohtype-177c22a15b5b
* Your code should document itself: https://www.youtube.com/watch?v=JQ8RQru-Y9Y
  