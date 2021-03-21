import requests
import codecs
from bs4 import BeautifulSoup as BS

import json

# 1. <div id="pjax-job-list">
# 2. <div class="card card-hover card-visited wordwrap job-link"> -> job-link




headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
           
domain = 'https://www.work.ua'
url = 'https://www.work.ua/ru/jobs-kyiv-python/'

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



# h = codecs.open('work.json', 'w', 'utf-8')
# h.write(str(jobs))
# h.close()
with codecs.open('work.json', 'w', 'utf-8') as file:
    json.dump(jobs, file, ensure_ascii=False, indent=4)