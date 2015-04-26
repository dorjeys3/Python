from lxml import html
import requests

page = requests.get('http://en.wikipedia.org/wiki/List_of_colors:_A%E2%80%93F') #get request from website
tree = html.fromstring(page.text) #set up tree formation to access data

Colors = tree.xpath('//div[@')