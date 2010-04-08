"""gitegginfo

Create a distribution's .egg-info directory and contents, pulling version
information from git or git-svn if possible."""

import os, re
from distutils.errors import DistutilsOptionError
from distutils import log
from pkg_resources import parse_requirements, safe_name, parse_version, \
    safe_version, iter_entry_points, to_filename

from setuptools.command.egg_info import egg_info, manifest_maker, \
    get_pkg_info_revision

from gitegginfo.revision import get_gitsvn_revision

class git_egg_info(egg_info):
    description = "create a distribution's .egg-info directory"

    user_options = [
        ('egg-base=', 'e', "directory containing .egg-info directories"
                           " (default: top of the source tree)"),
        ('tag-revision', 'r',
            "Add revision ID to version number"),
        ('tag-date', 'd', "Add date stamp (e.g. 20050528) to version number"),
        ('tag-build=', 'b', "Specify explicit tag to add to version number"),
        ('no-revision', 'R',
            "Don't add revision ID [default]"),
        ('no-date', 'D', "Don't include date stamp [default]"),
    ]

    boolean_options = ['tag-date', 'tag-revision']
    negative_opt = {'no-revision': 'tag-revision',
                    'no-date': 'tag-date'}


    def initialize_options(self):
        self.egg_name = None
        self.egg_version = None
        self.egg_base = None
        self.egg_info = None
        self.tag_build = None
        self.tag_revision = 0
        self.tag_date = 0
        self.broken_egg_info = False
        self.vtags = None

    def save_version_info(self, filename):
        from setopt import edit_config
        edit_config(
            filename,
            {'egg_info':
                {'tag_revision':0, 'tag_date': 0, 'tag_build': self.tags()}
            }
        )

    def finalize_options(self):
        self.egg_name = safe_name(self.distribution.get_name())
        self.vtags = self.tags()
        self.egg_version = self.tagged_version()

        try:
            list(
                parse_requirements('%s==%s' % (self.egg_name,self.egg_version))
            )
        except ValueError:
            raise DistutilsOptionError(
                "Invalid distribution name or version syntax: %s-%s" %
                (self.egg_name,self.egg_version)
            )

        if self.egg_base is None:
            dirs = self.distribution.package_dir
            self.egg_base = (dirs or {}).get('',os.curdir)

        self.ensure_dirname('egg_base')
        self.egg_info = to_filename(self.egg_name)+'.egg-info'
        if self.egg_base != os.curdir:
            self.egg_info = os.path.join(self.egg_base, self.egg_info)
        if '-' in self.egg_name: self.check_broken_egg_info()

        # Set package version for the benefit of dumber commands
        # (e.g. sdist, bdist_wininst, etc.)
        #
        self.distribution.metadata.version = self.egg_version

        # If we bootstrapped around the lack of a PKG-INFO, as might be the
        # case in a fresh checkout, make sure that any special tags get added
        # to the version info
        #
        pd = self.distribution._patched_dist
        if pd is not None and pd.key==self.egg_name.lower():
            pd._version = self.egg_version
            pd._parsed_version = parse_version(self.egg_version)
            self.distribution._patched_dist = None

    def tagged_version(self):
        return safe_version(self.distribution.get_version() + self.vtags)

    def run(self):
        self.mkpath(self.egg_info)
        installer = self.distribution.fetch_build_egg
        for ep in iter_entry_points('egg_info.writers'):
            writer = ep.load(installer=installer)
            writer(self, ep.name, os.path.join(self.egg_info,ep.name))

        # Get rid of native_libs.txt if it was put there by older bdist_egg
        nl = os.path.join(self.egg_info, "native_libs.txt")
        if os.path.exists(nl):
            self.delete_file(nl)

        self.find_sources()

    def tags(self):
        version = ''

        if self.tag_build:
            version+=self.tag_build

        if self.tag_revision:
            rev = get_gitsvn_revision()
            version += '-r%s' % rev

        if self.tag_date:
            import time
            version += time.strftime("-%Y%m%d")

        return version

