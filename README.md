# Netcraft-Programming-Test
Implement a very simple web crawler with the following task.

<u>**Tasks:** </u> 
1. Accept a single starting URL such as https://news.ycombinator.com as input.
2. Download the web page available at the input URL and extract URLs of the other pages linked to from the HTML source code.
3. Looking at the href attribute of tags to extract the links.
4. It should attempt to download each of those URLs in turn to find even more URLs, then download those and so on.

<u>**Goal:** </u> <br>
This program should stop after it has discovered 100 unique URLs and print one URL per line as its output.

## Table of Contents
- [Installation](#installation)
- [Scrapy Intro](#intro)
- [Web Crawl](#Explaination)
---
## Installation
This program required `Python version 3.7` and open-source web-crawling framework `Scrapy 2.2.0`

- Install Scrapy with `conda`:
```shell
C:\Users\User> conda install -c conda-forge scrapy
```

- Install Scrapy with its dependencies from `PyPI` with:
```shell
C:\Users\User> pip install scrapy
```
---
## Scrapy Intro
The Scrapy project can be created using **Scrapy Shell** command:
`dir/scrapy_project> scrapy startproject myproject [project_dir]`

The project directories will be created as follow:
<pre> _myproject/
├── scrapy.cfg
├── _project_dir/
    └── __init__.py
    └── items.py
    └── middlewares.py
    └── pipelines.py
    └── settings.py
    └── _spiders/
        └──__init__.py
</pre>

| file/folder | functionality |
|-------------|:--------------|
| scrapy.cfg  | deploy configuration file |
| lego_brick/ | Python project module where all the code are executed |
| __init__.py | Python module initialisation file |
| items.py    | project items file using feed export to generate JSON file |
| settings.py | project settings file |
| spider/     | Directory where web spider located |
| __init__.py | web spider initialsation file |

However, there are only two important files need to be modified:
1. settings.py - This file contains the settings responsible for the spider bot behaviors.
    * Set user agent to prevent block by robots.txt
    * Obey the rule set in the robots.txt by the scraped websites.
    * Enable concurrent request for multiple URLs.
    * Export the extracted URLs in CSV, Excel and JSON etc format.
2. spiders/ - This folder is where the custom spiders stored.
    * Create new spider bot with basic template by calling the command below <br>
    `./spider/:~$ scrapy genspider spiderbot "Given URLs"`
    * Initilise the spider by calling the command below <br>
    `./spider/:~$ scrapy crawl spiderbot`    
---
## Web Crawl
The settings default:
