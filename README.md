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
- [Scrapy Intro](#scrapy-intro)
- [Settings](#settings)
- [Web Crawl](#web-crawl)
- [URLs Output](#urls-output)
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
| spiders/     | Directory where web spider located |
| __init__.py | web spider initialsation file |

However, there are only two important files need to be modified:
1. settings.py - This file contains the settings responsible for the spider bot behaviors.
    * Set user agent to prevent block by robots.txt
    * Obey the rule set in the robots.txt by the scraped websites.
    * Enable concurrent request for multiple URLs.
    * Export the extracted URLs in CSV, Excel and JSON etc format.
2. spiders/ - This folder is where the custom spiders stored.
    * Create new spider bot with basic template by calling the command below <br>
    `./myproject/> scrapy genspider spiderbot "Given URLs"`
    * Initilise the spider by calling the command below <br>
    `./myproject/> scrapy crawl spiderbot`    
---
## Settings
In order to prevent being blocked by the webpages, there are conditions should be fulfilled to scrape politely.
- Do not fetch pages too quickly (add some download delay)
- Do send multiple requests at the same time (configure concurrent request)
- Some webpage has blocked scrapebot specified in robots.txt (try to set user-agent)
- Obey robots.txt

Configure parameter in settings.py:
``` python
USER_AGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
ROBOTSTXT_OBEY = True
CONCURRENT_REQUESTS = 1
DOWNLOAD_DELAY = 3
```
---
## Web Crawl
<p align="center">
  <img src="/crawl_page.jpg">
</p>
We can start scraping the URLs by running the command: `./myproject/> scrapy crawl web_crawler`. By default, Scrapy use a LIFO queue for storing pending request, which means that it crawls in depth-first order (**DFO**). Here is an example: <br>

1. Let suppose we have a base URL a1 <br>
a1 has three links: b1, b2, b3 <br>
2. Click on b1 bring us to the page <br>
b1 has three links: c1, c2, c3 <br>
3. Click on c1 bring us to the page <br>
c1 has three links: d1, d2, d3 <br>

In **DFO** manner, the crawler move as follow: <br>
a1, b1, b2, b3, c1, c2, c3, ... <br>

In **BFO** manner, the crawler move as follow: <br>
a1, b1, c1, c2, c3, b2, ..., b3 <br>

Here is the documentation if you want to configure to be breadth-first order (**BFO**): https://docs.scrapy.org/en/latest/topics/settings.html#depth-priority

---
## URLs Output
To simplify the work, 100 unique URLs are extracted and write into csv file shown in `Unique_url.csv`. 

The reason of doing this is because:
- Printing URLs in console are hardly to be seen when Scrapy request callback to fetch new links `[scrapy.spidermiddlewares.offsite] DEBUG: Filtered offsite request to`. 
- Using command `scrapy crawl web_crawler -o unique_url.json` will yield duplicate request URLs.
---
