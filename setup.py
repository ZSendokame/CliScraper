from setuptools import setup

long_description = open('./README.md')

setup(
    name='CliScrape',
    version='1.0.2',
    url='https://github.com/ZSendokame/CliScrapper',
    license='MIT license',
    author='ZSendokame',
    description='Webscrapping from the Terminal.',
    long_description=long_description.read(),
    long_description_content_type='text/markdown',
    py_modules=[
        'source.cs',
    ],

    entry_points={
        'console_scripts': [
            'cscrape=source.cs:main'
        ]
    },

    classifiers=[
        'Environment :: Web Environment',
    ]
)
