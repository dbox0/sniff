from urllib.request import urlopen

url = "http://funnyjunk.com/"

page = urlopen(url)
html_bytes = page.read()


html = html_bytes.decode("utf-8")
title_index = html.find("<title>")
title_start = title_index + len("<title>")
title_end = html.find("</title>")

title = html[title_start:title_end]
print(title)


#print(html)

