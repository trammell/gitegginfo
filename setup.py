from setuptools import setup, find_packages

setup_args=dict(
    name='gitegginfo',
    version='0.3',
    description="""\
    Setuptools extensions for git compatibility.

    See the project home page at http://github.com/trammell/gitegginfo for
    details.
    """,
    long_description=open('readme.rst').read() + '\n\n' + \
        open('history.txt').read() + '\n',
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='setuptools egg_info git',
    author='John Trammell',
    author_email='johntrammell@gmail.com',
    url='http://github.com/trammell/gitegginfo',
    license='GPL',
    packages=find_packages('lib'),
    package_dir = {'':'lib'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
    ],
    entry_points = {
        "distutils.commands": [
            "gitegginfo = gitegginfo.commands:gitegginfo",
            "gitsdist = gitegginfo.commands:gitsdist",
        ],
    },
    test_suite = 'tests.test_suite',
)

setup(**setup_args)
