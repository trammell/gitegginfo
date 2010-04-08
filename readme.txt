Intro
=====

This package is an extension of setuptools' egg_info command.  Where the
egg_info command is unwisely specific to the Subversion version control
system, the gitegginfo command is unwisely and explicitly tied to the Git
DVCS (distributed version control system).

To build an ``.egg-info`` folder with ``git-svn`` revision data:

::

   python setup.py gitegginfo -r

