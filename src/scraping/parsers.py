import requests
import codecs
from bs4 import BeautifulSoup as BS
from random import randint

import json




__all__ = ('work', 'rabota', 'dou', 'djinni')




headers = [
            {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
            {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
            {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:53.0) Gecko/20100101 Firefox/53.0',
             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
]
           


def work(url):
    jobs = []
    errors = []
    domain = 'https://www.work.ua'
    url = 'https://www.work.ua/ru/jobs-kyiv-python/'
    resp = requests.get(url, headers=headers[randint(0, 2)])
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
    return jobs, errors
            
def rabota(url):
    jobs = []
    errors = []
    domain = 'https://www.rabota.ua'
    #url = 'https://rabota.ua/zapros/python/%D0%BA%D0%B8%D0%B5%D0%B2'
    resp = requests.get(url, headers=headers[randint(0, 2)])
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        new_jobs = soup.find('div', attrs={'class': 'f-vacancylist-newnotfound'})
        if not new_jobs:
            table = soup.find('table', id='ctl00_content_vacancyList_gridList')
            if table:
                tr_list = table.find_all('tr', attrs={'id': True})
                for tr in tr_list:
                    div = tr.find('div', attrs={'class': 'card-body'})
                    if div:
                        #title = div.find('p', attrs={'class': 'card-title'})
                        title = div.find('h2', attrs={'class': 'card-title'})
                        href = title.a['href']
                        #content = div.p.text
                        content = div.find('div', attrs={'class': 'card-description'}).text                    
                        p = div.find('p', attrs={'class': 'company-name'})
                        company = p.a.text
                        # if p:
                            # company = p.a.text
                        jobs.append({
                            'title': title.text,
                            'url': domain + href,
                            'description': content,
                            'company': company
                        })                    
            else:
                errors.append({
                    'url': url,
                    'title': "TABLE doesn't exists!"
                })
        else:
            errors.append({
                    'url': url,
                    'title': "Page is empty!"
                })
    else:
        errors.append({
            'url': url,
            'title': "Page doesn't response!"
        })
    return jobs, errors
    
def dou(url):
    jobs = []
    errors = []
    #domain = 'https://jobs.dou.ua'
    #url = 'https://jobs.dou.ua/vacancies/?category=Python&search=%D0%9A%D0%B8%D0%B5%D0%B2'
    resp = requests.get(url, headers=headers[randint(0, 2)])
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        main_div = soup.find('div', id='vacancyListId')
        if main_div:
            li_list = main_div.find_all('li', attrs={'class': 'l-vacancy'})
            for li in li_list:
                title = li.find('div', attrs={'class': 'title'})
                href = title.a['href']
                cont = li.find('div', attrs={'class': 'sh-info'})
                content = cont.text
                company = 'No name'
                a = title.find('a', attrs={'class': 'company'})
                if a:
                    company = a.text
                jobs.append({
                    'title': title.text,
                    'url': href,
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
    return jobs, errors
    
def djinni(url):
    jobs = []
    errors = []
    domain = 'https://djinni.co'
    #url = 'https://djinni.co/jobs/keyword-python/kyiv/'
    resp = requests.get(url, headers=headers[randint(0, 2)])
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        main_ul = soup.find('ul', attrs={'class': 'list-jobs'})
        if main_ul:
            li_list = main_ul.find_all('li', attrs={'class': 'list-jobs__item'})
            for li in li_list:
                title = li.find('div', attrs={'class': 'list-jobs__title'})
                href = title.a['href']
                cont = li.find('div', attrs={'class': 'list-jobs__description'})
                content = cont.text
                company = 'No name'
                comp = li.find('div', attrs={'class': 'list-jobs__details__info'})
                if comp:
                    company = comp.text
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
    return jobs, errors



if __name__ == '__main__':
    url = 'https://djinni.co/jobs/keyword-python/kyiv/'
    jobs, errors = djinni(url)
    with codecs.open('djinni.json', 'w', 'utf-8') as file:
        json.dump(jobs, file, ensure_ascii=False, indent=4)