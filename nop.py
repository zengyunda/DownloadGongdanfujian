import re
import requests
import urllib
text = '<td class="content">YN-12345-160918-00062</td>'
resule = re.compile('<td class="content">(.*?)</td>').findall(text)[0]
print(resule)

gd ="url: 'itrequirementmanage.do?method=showSheetDealList&sheetKey=8a2d80be5739da6201573c2b433f1580&taskName=&ifWaitForSubTask='}"

print(re.compile("url: '(.*?)'\}",re.S).findall(gd)[0])

for page in range(1,55):
    Allgdresponse = requests.get(url=url+str(page)+'confidn+',headers=headers,cookies=cookies)#获取每页中的工单信息
    MainId = re.compile('<td class="content">(.*?)</td>').findall(Allgdresponse.text)#提取每页工单的mainid
    gdNum = re.compile('<td class="content">(.*?)</td>').findall(Allgdresponse.text)#提取工单号
    dictgd = zip(MainId,gdNum)#把工单号和mainid构建成字典，用于后续获取工单号
    for mainid in MainId:
        Eachdgresponse = requests.get(url=url+mainid,headers=headers,cookies=cookies)#获取每个工单里面的内容
        EachgdID = re.compile("url: '(.*?)'\}",re.S).findall(Eachdgresponse.text)[0]#匹配工单中的流转信息（附件在流转信息的url中）
        Eachgdfj = requests.get(url=url+EachgdID,headers=headers,cookies=cookies)#获取工单附件链接
        EachgdfjId = re.compile("url: '(.*?)'\}",re.S).findall(Eachgdfj.text)#匹配工单附件链接结果，返回列表
        MainIdfj = re.compile('var mainId = "(.*?)"',re.S).findall(Eachgdfj.text)[0]#获取附件里面MainId，用于匹配工单号
        if len(EachgdfjId) >0:#判断是否有链接，如果有链接则进行下载并保存
            for fjId in EachgdfjId:
                filename = 'D:/gdfj/'+dictgd[MainIdfj]#保存路径，以工单号开通
                urllib.urlretrieve(url+fjId, filename+'文件名')
        else:
            pass








fj = "nodeAccessories" class="uploadframe" frameborder="0" scrolling="auto" src="/eoms35/accessories/pages/view.jsp?appId=itrequirementmanage&filelist='20161009113256964.docx'&idField=nodeAccessories&startsWith=0" style="height:80%;width:100%"></iframe>"