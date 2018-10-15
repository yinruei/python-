from urllib.parse import urlparse
url = "https://taqm.epa.gov.tw/pm25/tw/PM25A.aspx?area=1"
o = urlparse(url)
print(o)

print("scheme={}".format(o.scheme))#http
print("netloc={}".format(o.netloc))#taqm.epa.gov.tw
print("port={}".format(o.port))#None
print("path={}".format(o.path))#/pm25/tw/PM25A.aspx
print("query={}".format(o.query))#area=1
# print("params={}".format(o.params))#
# print("fragment={}".format(o.fragment))#

