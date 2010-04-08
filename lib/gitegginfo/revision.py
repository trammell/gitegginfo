"""gitegginfo

Create a distribution's .egg-info directory and contents, pulling version
information from git or git-svn if possible."""

from subprocess import Popen, PIPE
from setuptools.command.egg_info import get_pkg_info_revision


def get_git_revision(self):
    """Try to pull a suitable revision number from 'git-describe'."""
    revision = 0

def get_gitsvn_info():
    """Returns a dict containing the output from 'git-svn info'."""
    try:
        d = {}
        p = Popen(['git-svn', 'info'], stdout=PIPE, stderr=PIPE)
        p.stderr.close()
        for line in p.stdout.readlines():
            (name,value) = line.split(":",1)
            d[name] = value
        return d
    except:
        return {}

def get_gitsvn_revision():
    """Try to pull a suitable revision number from 'git-svn info'."""
    rev = get_gitsvn_info().get("Revision",0)
    return str(rev or get_pkg_info_revision())

