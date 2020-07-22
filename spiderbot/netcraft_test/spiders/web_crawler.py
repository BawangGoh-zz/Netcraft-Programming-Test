#############################################
# Netcraft assignment 
#############################################
'''
Assignment: 
Implement a very simple web crawler with the following task.

Tasks:
1) Accept a single starting URL such as https://news.ycombinator.com as input.
2) Download the web page available at the input URL and extract URLs of other pages
linked to from the HTML source code.
3) Looking at the href attribute of tags to extract the links.
4) It should attempt to donwload each of those URLs in turn to find even more URLs,
then download those and so on.

Goals:
Ths program should stop after it has discovered 100 unique URLs and print one URL per
line as its output.
'''
import csv
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from scrapy.exceptions import CloseSpider

class WebCrawlerSpider(CrawlSpider):
	# Name of the web crawler
	name = 'web_crawler'

	# A list of URLs to crawl with start URLs as base URLs
	allowed_domains = ['news.ycombinator.com']
	start_urls = ['http://news.ycombinator.com/']

	# Use set container class to store unique URLs
	visited_url = set()

	# # Set rule to only extract anchor tags inside //div, //li and //td
	# rule = [Rule(
	# 	        LinkExtractor(restrict_xpaths=[
	# 	        	"//td",
	# 	            "//div",
	# 	            "//li"]),
	# 	        callback='parse')
	# 		]

	'''Default parsing function to parse base URLs and retrieve the URLs of other webpage

	Args:
		response: HTML source code

	Returns:
		{URLs}:  URLs 
	'''
	def parse(self, response):
		'''Searching for news links by looking at the header with the 'a' and download the pages
		'''
		for link in response.xpath('//a'):
			''' Append ::attr(href) to css to extract link in the href of anchor tags.
			'''
			if len(self.visited_url) < 100:
				extract_URL = link.css('::attr(href)').extract_first()

				# Exclude story link begin with item?id=
				if not (extract_URL.startswith('http://') or extract_URL.startswith('https://')):
					continue

				# Add unvisited URL to set
				self.visited_url.add(extract_URL)

				yield {
					'URLs': extract_URL,
				}
			else:
				print('Number of URLs: ', len(self.visited_url))
				print('Print one URL per line')
				self.printURL(self.visited_url)
				self.saveURL(self.visited_url)

				# Close spider to stop crawling
				raise CloseSpider('100 unique URLs found')

		# Passing each page to parse items to retrieve more links
		for url in self.visited_url:
			yield scrapy.Request(
				url,
				callback=self.parse
			)

		''' Crawl multiple page by finding the load more button and invoke the callback function if
		the more links exist.
		'''
		NEXT_PAGE_SELECTOR = 'a[rel="next"]::attr(href)'
		next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()

		# Invoke callback parse function 
		if next_page:
			yield scrapy.Request(
				response.urljoin(next_page),
				callback=self.parse
			)

	'''Print one URLs per line
	
	Args:
		List of URLs

	Returns:
		One URLs per line
	'''
	def printURL(self, url_list):
		for url in url_list:
			print(url)

	'''Save URLs into csv format
	
	Args:
		List of URLs

	Returns:
		CSV file 
	'''
	def saveURL(self, url_list):
		with open('Unique_url.csv', 'w', newline='') as csv_file:
			csv_writer = csv.writer(csv_file, delimiter='\n')
			csv_writer.writerow(url_list)
