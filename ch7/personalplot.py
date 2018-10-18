import matplotlib.pyplot as plt
from bs4 import BeautifulSoup as bs
import requests

year = []
person = []
url = "http://www.daxi-hro.tycg.gov.tw/home.jsp?id=25&parentpath=0,21,22"
content = requests.get(url).text
parse = bs(content, "html.parser")
data1 = parse.select("table[summary^='歷年戶數統計列表排版用']")[0]
rows = data1.find_all("tr")
print(rows)
for row in rows:
    cols = row.find_all("td")
    if(len(cols) > 0):
        if cols[1].text!="─":
            year.append(cols[0].text[:-1])
            person.append(cols[1].text)
plt.plot(year, person, linewidth=2.0)
plt.title("Number of households in Daxi District of Taoyuan City")
plt.xlabel("year")
plt.ylabel("Number of households")
plt.show()