import requests,xlwt,os
from bs4 import BeautifulSoup
from lxml import etree
from fake_useragent import UserAgent

ua = UserAgent()
headers = {'User-Agent': ua.random}
job = []
location = []
company = []
salary = []
link = []

for k in range(1, 10):
    url = 'http://www.shixiseng.com/interns?k=python&p=' + str(k)
    r = requests.get(url, headers=headers).text
    s = etree.HTML(r)
    job1 = s.xpath('//a/h3/text()')
    location1 = s.xpath('//span/span/text()')
    company1 = s.xpath('//p/a/text()')
    salary1 = s.xpath('//span[contains(@class,"money_box")]/text()')
    link1 = s.xpath('//div[@class="job_head"]/a/@href')
    for i in link1:
        url = 'http://www.shixiseng.com' + i
        link.append(url)
    salary11 = salary1[1::2]
    for i in salary11:
        salary.append(i.replace('\n\n', ''))
    job.extend(job1)
    location.extend(location1)
    company.extend(company1)

detail = []
for i in link:
    r = requests.get(i, headers=headers).text
    soup = BeautifulSoup(r, 'lxml')
    word = soup.find_all(class_="dec_content")
    for i in word:
        a = i.get_text()
        detail.append(a)

book = xlwt.Workbook()
sheet = book.add_sheet('sheet', cell_overwrite_ok=True)
path = 'D:\\Pycharm\\spider'
os.chdir(path)

j = 0
for i in range(len(job)):
    try:
        sheet.write(i + 1, j, job[i])
        sheet.write(i + 1, j + 1, location[i])
        sheet.write(i + 1, j + 2, company[i])
        sheet.write(i + 1, j + 3, salary[i])
        sheet.write(i + 1, j + 4, link[i])
        sheet.write(i + 1, j + 5, detail[i])
    except Exception as e:
        print('出现异常：' + str(e))
        continue
book.save('d:\\python.xls')
