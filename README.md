<div align="center">

# CliScrapper

CliScrapper makes Web Scrapping **simple** and **accessible from the Terminal**.

[Installation](#Installation) •
[How to use](#How-to-use)
</div>

## Installation
```sh
# Git
git clone https://github.com/ZSendokame/CliScrapper
cd CliScrapper
pip install requirements.txt

# Pip
# Working on that
```

## How to use
You have a lot of parameters!
```sh
python cs.py --url https://sendokame.netlify.app --tag "a" --output "text" # <- You can select the attributes of BS4. 
```
Or
```sh
python cs.py --url https://alansierra.xyz/blog/ --selector 'a > h2' --output text
```