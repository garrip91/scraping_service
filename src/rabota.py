import requests
import codecs
from bs4 import BeautifulSoup as BS

import json

# 1. <table class="f-vacancylist-tablewrap" ...>
# 2. <tr id="..."> -> <div class="card-body">

# 3. <p class="card-title">
# 4. <div class="card-description">




headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
           
domain = 'https://www.rabota.ua'
url = 'https://rabota.ua/zapros/python/%D0%BA%D0%B8%D0%B5%D0%B2'
'''
resp = requests.get(url, headers=headers)
jobs = []
errors = []
if resp.status_code == 200:
    soup = BS(resp.content, 'html.parser')
    main_div = soup.find('div', id='pjax-job-list')
    if main_div:
        div_list = main_div.find_all('div', attrs={'class': 'job-link'})
        for div in div_list:
            title = div.find('h2')
            href = title.a['href']
            content = div.p.text
            company = 'No name'
            logo = div.find('img')
            if logo:
                company = logo['alt']
            else:
                company = div.find('div', attrs={'class': 'add-top-xs'}).span.b.text
            jobs.append({
                'title': title.text,
                'url': domain + href,
                'description': content,
                'company': company
            })
    else:
        errors.append({
            'url': url,
            'title': "DIV doesn't exists!"
        })
else:
    errors.append({
            'url': url,
            'title': "Page doesn't response!"
        })



with codecs.open('rabota.json', 'w', 'utf-8') as file:
    json.dump(jobs, file, ensure_ascii=False, indent=4)
'''
resp = requests.get(url, headers=headers)

with codecs.open('rabota.html', 'w', 'utf-8') as file:
    file.write(str(resp.text))