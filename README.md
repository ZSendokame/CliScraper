<div align="center">

# CliScraper

CliScraper makes Web Scraping **simple** and **accessible from the Terminal**.<br>
[![PyPi Version](https://img.shields.io/pypi/v/CliScrape.svg?logo=pypi&logoColor=yellow)](https://pypi.org/project/CliScrape)
[![PyPi Downloads](https://img.shields.io/pypi/dm/CliScrape?logo=pypi&logoColor=yellow)](https://pypistats.org/packages/CliScrape)

[Installation](#Installation) •
[How to use](#How-to-use)
</div>

## Installation
```sh
# Git
git clone https://github.com/ZSendokame/CliScraper
cd CliScraper
pip install requirements.txt

# Pip
pip install CliScrape
```

## How to use
You have a lot of parameters!
```sh
cscrape --url https://sendokame.netlify.app --tag "a" --output "text" # <- You can select the attributes of BS4. 
```
Or
```sh
cscrape --url https://alansierra.xyz/blog/ --selector 'a > h2' --output text
```