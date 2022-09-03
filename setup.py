from setuptools import setup

long_description = open('./README.md')

setup(
    name='CliScrape',
    version='1.0.0',
    url='https://github.com/ZSendokame/CliScraper',
    license='MIT license',
    author='ZSendokame',
    description='Webscraping from the Terminal.',
    long_description=long_description.read(),
    long_description_content_type='text/markdown',

    entry_points={
        'console_scripts': [
            'cscrape=cliscraper.cs:main'
        ]
    },
)