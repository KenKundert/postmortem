#!/usr/bin/env python

from setuptools import setup
from codecs import open

with open('README.rst', encoding='utf-8') as f:
    readme = f.read()

setup(
    name = 'postmortem',
    version = '0.8.0',
    author = 'Ken Kundert',
    author_email = 'postmortem@nurdletech.com',
    description = 'Produces a package of information for dependents and partners to be opened upon death.',
    long_description = readme,
    long_description_content_type = 'text/x-rst',
    url = 'https://github.com/kenkundert/postmortem',
    download_url = 'https://github.com/kenkundert/postmortem/tarball/master',
    license = 'GPLv3+',
    scripts = 'postmortem'.split(),
    install_requires = [
        'appdirs',
        'avendesora>=1.14',
        'arrow',
        'docopt',
        'inform>=1.16',
        'nestedtext>=3.0',
        'python-gnupg>=0.4.4',
            # Be careful.  There's a package called 'gnupg' that's an 
            # incompatible fork of 'python-gnupg'.  If both are installed, the 
            # user will probably have compatibility issues.
        'voluptuous',
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
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Utilities',
    ],
)
