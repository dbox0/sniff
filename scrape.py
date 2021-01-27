from urllib.request import urlopen
import re

url = "http://www.webmfiles.org/demo-files/"

page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")

def getTitle():
	title_index = html.find("<title>")
	title_start = title_index + len("<title>")
	title_end = html.find("</title>")
	title = html[title_start:title_end]
	print(title)



def getBody():
	body_index = html.find("<body>")
	body_start = body_index + len("<body.")
	body_end = html.find("</body>")
	body = html[body_start:body_end]
	return body

def printbody():
	body = getBody()
	print(body)

def findwebm():
	body = getBody()
	webms  = re.findall(".webm",body)
	print(webms)

#print(html)

