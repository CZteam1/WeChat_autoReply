#_*_ coding:utf-8 _*_
#__author__='陈博楠'
#__date__ = '2018-03-28'
import json
import requests
def getPackages(packageNum):
    try:
        #输入运单号码：
        url1 = 'http://www.kuaidi100.com/autonumber/autoComNum?resultv2=1&text=' + packageNum
        #用url1查询运单号对应的快递公司，如中通，返回：zhongtong。
        companyName = json.loads(requests.get(url1).text)['auto'][0]['comCode']
        #在用url2查询和运单号、快递公司来查询快递详情，结果是一个json文件，用dict保存在resultdict中。
        url2 = 'http://www.kuaidi100.com/query?type=' + companyName + '&postid=' + packageNum#如：'&temp=0.9829438147420106'
        str='该快递号对应的快递公司：'
        print(str + companyName)
        print('时间↓                             地点和跟踪进度↓\n')
        details = "时间↓--地点和跟踪进度↓\n'"
        #print(json.loads(requests.get(url2).text))
        resultdict = json.loads(requests.get(url2).text)['data']
        for item in resultdict:
            str2 = item['time']+item['context']+'\n'
            #print(str2)
            details += str2
        return details
    except Exception as e:
        details = "运单号码有误"+repr(e)
    finally:
        return details
#if __name__=="__main__":
