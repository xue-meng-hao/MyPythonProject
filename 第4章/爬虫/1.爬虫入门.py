import requests

# 定义url
target_url = "https://www.tiobe.com/tiobe-index/"
# 发送请求，获取数据
response = requests.post(target_url)
# with open("tiobe.html","w",encoding="utf-8") as f:
#     f.write(response.text)
# print(response.text)


from lxml import html

document = html.fromstring(response.text)

table = document.xpath('//table[@id="top20"]/thead/tr/th/text()')
print(table)
tr_list = document.xpath('//table[@id="top20"]/tbody/tr')
for tr in tr_list:
    print(tr.xpath('./td/text()'))

# aa=document.xpath('//*[@id="top20"]/tbody/tr')
# for a in aa:
#     print(a.xpath('./td/text()'))

# top20=document.xpath('//td[@class="td-top20"]/img/@src')
# print(top20)

# 读取html文件
# with open("tiobe.html", "r", encoding="utf-8") as f:
#     html_content = f.read()
#     # print(html_content)
#     tree = html.fromstring(html_content)
#     # print(tree.xpath('//*[@id="main"]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/div[1]/div[1]/div[1]/div/div[1]/div/text()'))
#     print(tree.xpath('//table/thead/tr/th/text()'))
#     tr_list = tree.xpath('//tbody/tr')
#     for tr in tr_list:
#         print(tr.xpath('./td/text()'))
#     # 匹配src属性
#     class1 = tr.xpath('//td[@class="td-top20"]/img/@src')
#     # 匹配所有属性
#     # class1 = tr.xpath('//td[@class]/img/@*')
#     print(class1)

# 爬虫解析说明:
# / 表示从根目录查找
# // 表示从任意位置查找
# . 表示当前目录
# [n] 表示选择第n个元素
# [last()] 表示选择最后一个元素
# [@attr] 表示标签包含属性attr,如 //p[@color]
# [@attr='value'] 表示属性值等于指定的元素，如：//p[@color='red']
# * 匹配任意字符,如//body/div/*
# @* 表示任意属性，如 //body/div/a/@*
# text()表示字符串，//div/p/text()
