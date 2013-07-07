"""
Use setuptools instead of distutils as a build tool because it provides
out of the box integration with nose. MANFEST.in contains directives to
include additional files as part of build.
"""

from setuptools import setup

setup(
    description = 'My Project',
    author = 'My Name',
    url = 'URL to get it at.',
    download_url = 'Where to download it.',
    author_email = 'My email.',
    install_requires = ['nose'],
    packages = ['sample'],
    scripts = [],
    name = 'sample',
    version = '1.1',
    classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers'
    ]
)
