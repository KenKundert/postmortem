#!/usr/bin/env python

from setuptools import setup

with open('README.rst') as file:
    readme = file.read()

setup(
    name = 'postmortem',
    version = '0.2.0',
    author = 'Ken Kundert',
    author_email = 'postmortem@nurdletech.com',
    description = 'Produces a package of information for dependents and partners to be opened upon death.',
    long_description = readme,
    url = 'https://github.com/kenkundert/postmortem',
    download_url = 'https://github.com/kenkundert/postmortem/tarball/master',
    license = 'GPLv3+',
    scripts = 'postmortem'.split(),
    install_requires = [
        'appdirs',
        'avendesora>=1.12',
            # this should be >=1.13, but it is not out yet; grab the latest
            # version from github
        'arrow',
        'docopt',
        'inform>=1.14',
        'python-gnupg>=0.4.3',
            # Be careful.  There's a package called 'gnupg' that's an 
            # incompatible fork of 'python-gnupg'.  If both are installed, the 
            # user will probably have compatibility issues.
    ],
    python_requires='>=3.6',
    keywords = 'postmortem'.split(),
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities',
    ],
)
