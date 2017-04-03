#!/usr/bin/python
import requests
import urllib.request
from HandleJs import Py4Js
file=open("1.txt")
context=""
while 1:
    line=file.readline()
    context = context+line
    if not line:
        break
print(context)
def is_chinese(uchar):
    if uchar >=u'\u4e00' and uchar<=u'\u9fa5':
        return True
    else:
        return False
s=requests.Session();
#  context = input("请输入翻译文本: ")
#  print(is_chinese(context))
#  targe_lang=input("目标语言:")
if(is_chinese(context)=='True'):
    targe_lang="en"
else:
    targe_lang="zh-cn"



#  context=urllib.parse.quote(context)
js = Py4Js()
tk = js.getTk(context)
context=urllib.parse.quote(context)
print(len(context))
url="http://translate.google.cn/translate_a/single?client=t&sl=auto&tl=%s&hl=en&" \
    "dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&otf=1&" \
    "ssel=3&tsel=3&kc=3&tk=%s&q=%s"%(targe_lang,tk,context)
url2="http://translate.google.cn/translate_a/single?client=gtx&sl=auto&tl=en&dt=t&q=%s"%(context)

url3="http://translate.google.cn/translate_a/single?client=t&sl=auto&tl=%s&hl=en&" \
    "dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&otf=1&" \
    "ssel=3&tsel=3&kc=3&tk=%s"%(targe_lang,tk)
headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate, sdch',
            'Accept-Language':'en-US,en;q=0.8;zh-CN;q=0.6,zh;q=0.4',
            'Connection':'keep-alive',
            'DNT':'1',
            'Host':'translate.google.cn',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2987.133 Mobile Safari/537.36'
    }
#  r = s.post(url3,data=context,headers=headers)

r = s.get(url,headers=headers)
#  print(r.status_code)
result = r.text.split(",")[0]
result = result.lstrip('[]')
print(result)
