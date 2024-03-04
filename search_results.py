import requests, sys, webbrowser, bs4

query = ' '.join(sys.argv[1:])

print('Searching...' + query)    # display text while downloading the search result page

req = requests.get('https://pypi.org/search/?q='+ query)

req.raise_for_status()

soup = bs4.BeautifulSoup(req.text,'html.parser')

linkelems = soup.select('.package-snippet')

numopen = min(5, len(linkelems))

for i in range(numopen):    
    urlopen = 'https://pypi.org'+linkelems[i].get('href')
    print('Opening ...', urlopen)
    webbrowser.open(urlopen)

