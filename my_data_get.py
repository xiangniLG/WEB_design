import requests
import json

def get_data():
  url="https://piaofang.maoyan.com/getBoxList?date=1&isSplit=true"
  myheaders={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
  mydata=requests.get(url,headers=myheaders).text
  return mydata

mydata=json.loads(get_data())
print(mydata["status"])
