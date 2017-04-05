#!/usr/bin/python
import sys
import requests
import urllib.request
from HandleJs import Py4Js

def isChinese(uchar):
    if uchar >=u'\u4e00' and uchar<=u'\u9fa5':
        return 'True'
    else:
        return 'False'

def Translate(context):
    s=requests.Session()
    if(isChinese(context)=='True'):
        targe_lang="en"
    else:
        targe_lang="zh-cn"
    js = Py4Js()
    tk = js.getTk(context)
    context=urllib.parse.quote(context)
    url="http://translate.google.cn/translate_a/single?client=t&sl=auto&tl=%s&hl=en&" \
        "dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&otf=1&" \
        "ssel=3&tsel=3&kc=3&tk=%s&q=%s"%(targe_lang,tk,context)

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

    try:
        r = s.get(url,headers=headers)
        s.close()
    except request.exceptions.ConnectionError:
        print("Connect Error , jump the line\n")
        return "opp!!!"

    if(targe_lang=="zh-cn"):
        out=""
        result = r.text.split('"')
        loop = len(result)
        for a in range(1,int(loop/2-2)):
            if(result[a]=="en"):
                break
            if(isChinese(result[a])=='True'):
                out+=result[a]
        return out
    else:
        result = r.text.split(',')[0]
        result = result.lstrip('[]')
        return result

def saveResult(context):
    with open("result.txt",'a+') as f:
        f.write(context+'\n')
    f.close()

def fileTranslate(filename):
    #  with open(filename,'r',encoding='utf-8',errors='ignore') as f:
    try:
        f=open(filename,'r',encoding='utf-8',errors='ignore')
    except IOError:
        print("open failed, please check the filename")
    else:
        f.readline()
        for line in f:
            a = Translate(line)
            saveResult(a)

def main():
    for i in sys.argv[1:]:
        filename = i
        fileTranslate(filename)
        return 0

    context=input("please input the text:")
    a = Translate(context)
    print(a)

if __name__ == "__main__":
    main()
'''
    trans = input("if you want to translate file input 1 or input 2 :")
    if(trans=="1"):
        filename = input("please input filename:")
        fileTranslate(filename)
    else:
        context=input("please input the text:")
        a = Translate(context)
        print(a)
'''
