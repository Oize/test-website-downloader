from setuptools import setup, find_packages
from os.path import join, dirname
from barewebsite import __version__

setup(
    name = 'barewebsite',
    version = __version__,
    packages = find_packages(),
    long_description = open(join(dirname(__file__), 'README.txt')).read(),
    entry_points = {
        'console_scripts':
            ['barewebsite = barewebsite.core:print_message']
    }
)
