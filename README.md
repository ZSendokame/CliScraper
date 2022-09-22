<div align="center">

# CliScraper

![image](https://user-images.githubusercontent.com/70088953/191654614-f7b175c5-151a-4248-8d44-cdb3d3ae7eee.png)

CliScraper makes Web Scraping **simple** and **accessible from the Terminal**.<br>
[Installation](#Installation) •
[How to use](#How-to-use)
</div>

## Installation
```sh
pip install git+https://github.com/ZSendokame/CliScraper.git
```

## How to use
You have a lot of parameters!
```sh
cscrape --url https://sendokame.netlify.app --tag "a" # <- You can select the attributes of BS4. 
```
Or
```sh
cscrape --url https://alansierra.xyz/blog/ --selector 'a > h2'
```
<br>

There are filters!
```sh
                                            |Python oneline code that outputs Node attributes
cscrape --url https://example.com --tag "p" --filter "node.attrs"
                                   |You can use Tags or Selector
```
