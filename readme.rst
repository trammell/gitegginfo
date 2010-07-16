Intro
=====

This package is an extension of setuptools' egg_info command.  Where the
egg_info command is unwisely specific to the Subversion version control
system, the gitegginfo command is unwisely and explicitly tied to the Git
DVCS (distributed version control system).

To build an ``.egg-info`` folder with ``git-svn`` revision data:

::

   python setup.py gitegginfo -r

Troubleshooting
===============

If you run into the problem where setuptools isn't including all your code in
the created egg, you may need to install package ``setuptools-git``.
