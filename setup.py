from setuptools import setup

long_description = open('./README.md')

setup(
    name='CliScrape',
    version='1.0.0',
    url='https://github.com/ZSendokame/CliScrapper',
    license='MIT license',
    author='ZSendokame',
    description='Webscrapping from the Terminal.',
    long_description=long_description.read(),
    long_description_content_type='text/markdown',
    py_modules=['cs'],

    entry_points="""
        [console_scripts]
        cliscrapper=cs:main
    """,

    classifiers=[
        'Environment :: Web Environment',
    ]
)
