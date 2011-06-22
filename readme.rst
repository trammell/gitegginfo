==========
gitegginfo
==========

.. target-notes

Introduction
============

Package ``gitegginfo`` adds two setuptools_ commands to make it possible to use
setuptools with git repositories when building development eggs.  Problems
occur in that setuptools specifically looks for subversion_ revision numbers,
even when subversion is not the underlying SCM.

This package is intended for use with git-svn_, which I use as an interface
between git and subversion.

gitegginfo
----------

The ``gitegginfo`` command is an extension of setuptools' egg_info command.
Where the egg_info command is unwisely specific to the subversion_ version
control system, the gitegginfo command is unwisely and explicitly tied to the
Git DVCS (distributed version control system).

gitsdist
--------

The ``sdist`` command that comes with setuptools is used to





Sample Commands
===============

To build an ``.egg-info`` folder with ``git-svn`` revision data:

::

   python setup.py gitegginfo -r







Troubleshooting
===============

If you run into the problem where setuptools isn't including all your code in
the created egg, you may need to install package ``setuptools-git``.


Editorial
=========
As I write this, the Python packaging infrastructure is in a dismal state.


See Also
========

git_, git-svn_, setuptools_, setuptools_git_, subversion_

.. _distutils:      http://docs.python.org/distutils/index.html
.. _git:            http://git-scm.com/
.. _git-svn:        http://www.kernel.org/pub/software/scm/git/docs/git-svn.html
.. _setuptools:     http://pypi.python.org/pypi/setuptools
.. _setuptools_git: http://pypi.python.org/pypi/setuptools-git/0.3.3
.. _subversion:     http://en.wikipedia.org/wiki/Apache_Subversion
.. _sdist:          http://docs.python.org/distutils/sourcedist.html
