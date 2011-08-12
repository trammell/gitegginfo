==========
gitegginfo
==========

.. class:: center

A setuptools extension for git

:Author: John Trammell
:Date:   August 11th, 2011


context
=======

* $ork started using svn around 2007

.. class:: incremental

* tried development with ``git``, ``hg``, ``arch``

.. class:: incremental

* ended up staying with git for personal projects

    .. class:: incremental

    - private branches

    .. class:: incremental

    - network optional

    .. class:: incremental

    - github


incremental development
=======================

.. class:: incremental

    some.pkg-1.2.2.egg

.. class:: incremental

    some.pkg-1.2.3dev-r3141.egg

.. class:: incremental

    ...

.. class:: incremental

    some.pkg-1.2.3dev-r3210.egg

.. class:: incremental

    some.pkg-1.2.3.egg



~/.pydistutils.cfg
==================

::

    [aliases]
    dev = egg_info -rDb dev bdist_egg ...
    rel = egg_info -RDb ""  bdist_egg ...

.. class:: incremental

... until I learned about ``git-svn``...


what is git-svn?
================

bidirectional operation between an svn repository and git

::

    % git svn clone svn://host/my/repo/

.. class:: incremental

::

    ... edit files ...
    % git svn rebase    # pull in changes
    % git svn dcommit   # push changes

.. class:: incremental

http://www.kernel.org/pub/software/scm/git/docs/git-svn.html



build problem #1
================

Where are all my files?

.. class:: incremental

::

    "setuptools.file_finders":
        ["svn_cvs = setuptools.command.sdist:_default_revctrl"],

.. class:: incremental

looks in ``.svn/entries``

.. class:: incremental

setuptools-git ("gitlsfiles")




build problem #2
================

some.pkg-1.2.3dev-r0.egg

.. class:: incremental

* can't expect setuptools to know about git-svn

.. class:: incremental

* ``git svn info``
* ``egg_info`` => ``gitegginfo``

.. class:: incremental

::

    [aliases]
    dev    = egg_info   -rDb dev bdist_egg ...
    gitdev = gitegginfo -rDb dev bdist_egg ...



enter plone 4
=============

.. class:: incremental

Plone 2.x, 3.x require python **2.4**

.. class:: incremental

Plone 4.0 requires python **2.6**

.. class:: incremental

... but we have sites running both!

.. class:: incremental

::

    [aliases]
    ...
    gitdev = gitegginfo -rDb dev sdist ...



build problem #3
================

.. class:: incremental

Tarball contains ``setup.cfg``

.. class:: incremental

::

    [egg_info]
    tag_build = 
    tag_date = 0
    tag_svn_revision = 0

.. class:: incremental

``sdist`` is tied to svn, via ``egg_info``



sdist => gitsdist
=================

.. class:: incremental

Extended ``sdist`` to correctly populate ``setup.cfg``

.. class:: incremental

::

    [aliases]
    ...
    gitdev = gitegginfo -rDb dev gitsdist ...


question
========

What are best practices for distributing code **today**?

.. image:: state_of_packaging.jpg



questions
=========

.. class:: incremental

.. image:: come-at-me-bro-hedgehog.jpg

