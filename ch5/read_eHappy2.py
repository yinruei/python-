import requests
url = "https://taqm.epa.gov.tw/pm25/tw/PM25A.aspx"
html = requests.get(url)
html.encoding="urf-8"
htmllist = html.text.splitlines()
for row in htmllist:
    print(row)