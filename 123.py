import requests
headers=\
{
'Host': 'rdc28.cwb.gov.tw',
'Connection': 'keep-alive',
'Content-Length': '22',
'Accept': 'text/plain, */*; q=0.01',
'Origin': 'http://rdc28.cwb.gov.tw',
'X-Requested-With': 'XMLHttpRequest',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
'Content-Type': 'application/x-www-form-urlencoded',
'Referer': 'http://rdc28.cwb.gov.tw/TDB/ntdb/pageControl/ty_warning',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7'
}
data='year=all&model=warning'
web=requests.post('http://rdc28.cwb.gov.tw/TDB/ctrl_typhoon_list/get_typhoon_list_table',headers=headers,data=data)
web.encoding='utf-8'
with open(r'123.txt','w',encoding='utf-8') as Filetxt:
 Filetxt.write(web.text)