from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

dependencies = (
	'Django>=1.7,<1.8',
	'py2neo>=1.6.4,<1.7'	
)

setup(
    name='veternote',
    version='0.0.1',
    description='Notes for some kind of veterans',
    author='Vlad George Ardelean',
    author_email='de4sh@yahoo.com',
    packages=find_packages(),
    install_requires=dependencies,
    extras_require={'docs': ['Sphinx==1.2.2', 'sphinx-rtd-theme==0.1.6']},
    include_package_data=True,
#    cmdclass={'test': test},
)

