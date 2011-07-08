"""
Commands to getting git revision strings (from either git, or from the
underlying svn repository if using git-svn).

Also, found on http://peak.telecommunity.com/DevCenter/setuptools ::

    A post-release tag is either a series of letters that are alphabetically
    greater than or equal to "final", or a dash (-). Post-release tags are
    generally used to separate patch numbers, port numbers, build numbers,
    revision numbers, or date stamps from the release number. For example, the
    version 2.4-r1263 might denote Subversion revision 1263 of a post-release
    patch of version 2.4. Or you might use 2.4-20051127 to denote a
    date-stamped post-release.

The prefix "r-" is used to denote subversion postreleases, and the prefix "g-"
is used for git postreleases.
"""

from subprocess import Popen, PIPE
from setuptools.command.egg_info import get_pkg_info_revision


def get_git_description():
    """
    Use the output of 'git describe' as our revision number.  The output will
    look like <tag>-<commits>-<obj>, e.g. "1.0-14-g24a41ec".
    """
    # At some point when I understand the use cases better, may need to do some
    # manipulation of the description string to make a better version ID...
    try:
        #import pdb; pdb.set_trace()
        p = Popen(['git', 'describe', '--always'], stdout=PIPE, stderr=PIPE)
        p.stderr.close()
        desc = p.stdout.readlines()[0].strip()
        return desc
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
