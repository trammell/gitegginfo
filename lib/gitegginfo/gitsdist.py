from setuptools.command.sdist import sdist as st_sdist
from distutils.command.sdist import sdist as du_sdist

import os


class gitsdist(st_sdist):
    """
    Extends class ``setuptools.command.sdist``. This version should correctly
    create setup.cfg files for development eggs when using git for version
    control.
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
