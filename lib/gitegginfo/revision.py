"""
gitegginfo

Create a distribution's .egg-info directory and contents, pulling version
information from git or "git svn" if possible.
"""

from subprocess import Popen, PIPE
from setuptools.command.egg_info import get_pkg_info_revision


def get_git_description(self):
    """
    Try to pull a suitable revision number from the output of 'git describe'.
    The output will look like <tag>-<commits>-<obj>, e.g.  "v1.0-14-g2414721";
    to massage it into something that can be used, the following code strips
    off the tag portion of the description.
    """
    try:
        p = Popen(['git', 'describe', '--always'], stdout=PIPE, stderr=PIPE)
        p.stderr.close()
        rev = p.stdout.readlines()[0].strip().split('-')
        return "-".join(rev[1:])
    except:
        return None


def get_gitsvn_info():
    """
    Returns a dict containing the output from "git svn info".
    """
    try:
        d = dict()
        p = Popen(['git', 'svn', 'info'], stdout=PIPE, stderr=PIPE)
        p.stderr.close()
        for line in p.stdout.readlines():
            try:
                (name, value) = line.strip().split(":", 1)
                d[name.strip()] = value.strip()
            except ValueError:
                pass
        return d
    except:
        return dict()


def get_gitsvn_revision():
    """
    Pull the revision number from the output of the command 'git svn info'.
    """
    rev = get_gitsvn_info().get("Revision", 0)
    return str(rev or get_pkg_info_revision())
