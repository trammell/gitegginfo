"""
gitegginfo

Create a distribution's .egg-info directory and contents, pulling version
information from git or git-svn if possible.
"""

import os
from distutils.errors import DistutilsOptionError
from pkg_resources import parse_requirements, safe_name, parse_version, \
    safe_version, iter_entry_points, to_filename
from setuptools.command.egg_info import egg_info
from gitegginfo.revision import get_git_revision, get_gitsvn_revision


class git_egg_info(egg_info):

    def tags(self):
        """
        Customized version of tags() method to include git or git-svn revision
        if available.
        """
        version = ''

        if self.tag_build:
            version += self.tag_build

        if self.tag_revision:
            rev = get_git_revision()
            rev = get_gitsvn_revision()

            version += '-r%s' % rev

        if self.tag_date:
            import time
            version += time.strftime("-%Y%m%d")

        return version
