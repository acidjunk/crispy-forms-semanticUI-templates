import os
from setuptools import setup, find_packages

from crispy_forms_semantic_ui import __version__

APPNAME = 'crispy-forms-semantic-ui'

with open(os.path.join(os.path.dirname(__file__), APPNAME.replace('-','_'), 'README.rst')) as readme:
    README = readme.read()

setup(
    name=APPNAME,
    version='.'.join(map(str, __version__)),
    packages=find_packages(),
    include_package_data=True,
    license='GPLv3 License',
    description='Semantic UI templates for django-crispy-forms.',
    long_description=README,
    keywords='django crispy-forms semantic-ui forms',
    url='https://github.com/acidjunk/crispy-forms-semanticUI-templates',
    author='Rene Dohmen',
    author_email='acidjunk@gmail.com',
    install_requires=['django-crispy-forms', 'django'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
