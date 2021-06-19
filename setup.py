from setuptools import setup

# read the contents of README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    author='Dylan Richardson',
    author_email='dylanrichardson1996@gmail.com',
    
    maintainer='Alexandru Cristiean',
    maintainer_email='alexandru.cristiean@gmail.com',

    version='0.4.0',
    name='BracketMaker',
    packages=['bracket'],
    url='http://pypi.python.org/pypi/BracketMaker/',
    description='Create and store readable brackets.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',

    project_urls={
        'Source': 'https://github.com/cristiean/bracket',
    },

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ],

    entry_points={
        'console_scripts': [
            'bracket=bracket.bracket:run', # This should allow the user to run `$ bracket` in terminal, which should run the `run()` function in the `bracket/bracket.py`
        ],
    },
    
    scripts=['bin/main.py'],
)