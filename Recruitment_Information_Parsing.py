#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import lxml.etree
import os
import time
import re
import pandas as pd
xiangxi = [] #详细信息
mingcheng = [] #公司名称
zhiwei = [] #职位
xinxi = [] #岗位信息
dizhi = [] #公司地址
jianjie = [] #公司简介
gongzi = [] #工资
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
}
for page in range(1,11): ##11为爬取前10页，这个数据可以更改
    url = 'https://search.51job.com/list/030200,000000,0000,00,9,99,python,2,'+str(page)+'.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field='
    response = requests.get(url = url,headers = headers) #获取数据
    response.encoding='gbk' #解码
    page_text = response.text
    import re
    url = re.findall('"job_href":"(.*?)"',page_text,re.S)
    real_url = []
    for each in url:
        real_url.append(re.sub(r'\\/','/',each))
    for each in real_url:
        response = requests.get(url = each,headers = headers)
        response.encoding='gbk'
        page_text2 = response.text
        tree = lxml.etree.HTML(page_text2)
        try:
            xiangxi.append(" ".join('%s' %id for id in tree.xpath('//p[@class="msg ltype"]//text()')))
        except IndexError:
            xiangxi.append("没找到相关内容")
        try:
            mingcheng.append(tree.xpath('//p[@class="cname"]/a//text()')[0]) #公司名称
        except IndexError:
            mingcheng.append("没找到相关内容")
        try:
            zhiwei.append(tree.xpath('//div[@class="cn"]/h1//text()')[0])#招聘职位
        except IndexError:
            zhiwei.append("没找到相关内容")
        try:
            xinxi.append(" ".join('%s' %id for id in tree.xpath('//div[@class="bmsg job_msg inbox"]/p//text()'))) #岗位信息
        except IndexError:
            xinxi.append("没找到相关内容")
        try:
            dizhi.append(tree.xpath('//div[@class="bmsg inbox"]/p[@class="fp"]//text()')[1]) #地址
        except IndexError:
            dizhi.append("没找到相关内容")
        try:
            jianjie.append(" ".join('%s' %id for id in tree.xpath('//div[@class="tmsg inbox"]//text()'))) #公司简介
        except IndexError:
            jianjie.append("没找到相关内容")
        try:
            gongzi.append(tree.xpath('//div[@class="cn"]/strong//text()')[0])#工资
        except IndexError:
            gongzi.append("没找到相关内容")
dic1 = {'公司名称': mingcheng,
    '招聘职位':zhiwei,
    '工资':gongzi,
    '详细信息':xiangxi,
    '地址':dizhi,
    '岗位信息':xinxi,
    '公司简介':jianjie,
   }
df = pd.DataFrame(dic1)
df.to_excel('job_information.xlsx', index=False)

