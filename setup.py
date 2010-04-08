from setuptools import setup, find_packages

setup(
    name='gitegginfo',
    version='0.1',
    description="Setuptools extension to use Git version information",
    long_description=open('readme.txt').read() + '\n\n' + \
        open('history.txt').read() + '\n',
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='setuptools egg_info git',
    author='John Trammell',
    author_email='johntrammell@gmail.com',
    url='http://johntrammell.com',
    license='GPL',
    packages=find_packages('lib'),
    package_dir = {'':'lib'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'GitPython',
    ],
    entry_points = {
        "distutils.commands": [
            "gitegginfo = gitegginfo.egg_info:git_egg_info",
        ],
    },
    test_suite = 'tests.test_suite',

)
