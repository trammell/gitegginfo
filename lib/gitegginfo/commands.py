"""
Setuptools command definitions go here.
"""


import os
import time
from distutils.command.sdist import sdist as du_sdist
from setuptools.command.egg_info import egg_info
from setuptools.command.sdist import sdist as st_sdist
from gitegginfo.revision import get_git_description, get_gitsvn_revision


class gitegginfo(egg_info):
    """
    Class to implement the 'gitegginfo' command, which creates a distribution's
    .egg-info directory and contents, pulling version information from git or
    git-svn if possible.
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
            version += '-r%s' % rev     # e.g. 0.1dev-r12345

        elif self.tag_git_desc:
            rev = get_git_description()
            version += '-g.%s' % rev    # e.g. 0.1dev-g

        if self.tag_date:
            version += time.strftime("-%Y%m%d")

        return version


class gitsdist(st_sdist):
    """
    Class to implement the ``gitsdist`` command, by extending class
    ``setuptools.command.sdist``. This version should correctly create
    setup.cfg files for development eggs when using git for version control.
    """

    user_options = [
        ('formats=', None,
         "formats for source distribution (comma-separated list)"),
        ('keep-temp', 'k',
         "keep the distribution tree around after creating " +
         "archive file(s)"),
        ('dist-dir=', 'd',
         "directory to put the source distribution archive(s) in "
         "[default: dist]"),
        ]

    negative_opt = {}

    def run(self):
        """ """
        self.run_command('gitegginfo')
        ei_cmd = self.get_finalized_command('gitegginfo')
        self.filelist = ei_cmd.filelist
        self.filelist.append(os.path.join(ei_cmd.egg_info, 'SOURCES.txt'))
        self.check_readme()
        self.check_metadata()
        self.make_distribution()

        dist_files = getattr(self.distribution, 'dist_files', [])
        for file in self.archive_files:
            data = ('sdist', '', file)
            if data not in dist_files:
                dist_files.append(data)

    def make_release_tree(self, base_dir, files):
        """
        Extend distutils's make_release_tree method to include a
        correctly-formatted ``setup.cfg`` in the source distribution.
        """

        du_sdist.make_release_tree(self, base_dir, files)

        # Save any egg_info command line options used to create this sdist
        dest = os.path.join(base_dir, 'setup.cfg')
        if hasattr(os, 'link') and os.path.exists(dest):
            # unlink and re-copy, since it might be hard-linked, and
            # we don't want to change the source version
            os.unlink(dest)
            self.copy_file('setup.cfg', dest)

        self.get_finalized_command('gitegginfo').save_version_info(dest)
