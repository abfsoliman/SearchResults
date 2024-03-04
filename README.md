# Python Package Index Search Tool

## Description

Whenever you search for a topic on Google, you might find it tedious to manually open several search results in new tabs. This script automates this process specifically for the Python Package Index (PyPI) website.

Here's what the script does:

1- It retrieves search keywords from the command line arguments.

2- It fetches the search results page from PyPI using the requests module.

3- It extracts the links to each search result using BeautifulSoup.

4- Finally, it opens a browser tab for each search result using the webbrowser.open() function.

> Note: This script can be easily adapted to work with other websites as well.
> However, certain websites like Google and DuckDuckGo employ measures to prevent scraping their search results pages, making automation challenging.


## How to Use

1- Make sure you have Python installed on your system.
```
pip install requests beautifulsoup4
```
2- Install the required libraries by running:
```
python search_results.py your_search_query
```

Feel free to modify and expand upon this script to suit your needs or integrate it into other projects. Happy searching!
