# Netcraft-Programming-Test
Implement a very simple web crawler with the following task.

<u>**Tasks:** </u> 
1. Accept a single starting URL such as https://news.ycombinator.com as input.
2. Download the web page available at the input URL and extract URLs of the other pages linked to from the HTML source code.
3. Looking at the href attribute of tags to extract the links.
4. It should attempt to download each of those URLs in turn to find even more URLs, then download those and so on.

<u>**Goal:** </u> <br>
This program should stop after it has discovered 100 unique URLs and print one URL per line as its output.
