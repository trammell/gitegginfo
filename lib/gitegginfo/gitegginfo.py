"""
gitegginfo

Create a distribution's .egg-info directory and contents, pulling version
information from git or git-svn if possible.
"""

import time
from setuptools.command.egg_info import egg_info
from gitegginfo.revision import get_git_description, get_gitsvn_revision


class gitegginfo(egg_info):
    """
    Class to implement the 'gitegginfo' command.
    """

    user_options = list(egg_info.user_options)
    user_options += [('tag-git-desc', 'g',
        'Add git description to version number')]

    def initialize_options(self):
        """
        Call parent class to initialize standard options, then initialize new
        git-specific options.
        """
        egg_info.initialize_options(self)
        self.tag_git_desc = False

    def tags(self):
        """
        Customized version of tags() method to include git or git-svn revision
        if available.
        """
        version = ''

        if self.tag_build:
            version += self.tag_build

        if self.tag_svn_revision:
            rev = get_gitsvn_revision()
            version += '-r%s' % rev

        elif self.tag_git_desc:
            rev = get_git_description()
            version += '-r%s' % rev

        if self.tag_date:
            version += time.strftime("-%Y%m%d")

        return version
