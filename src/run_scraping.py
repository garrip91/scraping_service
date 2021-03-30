from scraping.parsers import *
import codecs
import json

#from scraping.models import Vacancy, City, Language

import os, sys
proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scraping_service.settings")
import django
django.setup()

from scraping.models import Vacancy, City, Language



parsers = (
    (work, 'https://www.work.ua/ru/jobs-kyiv-python/'),
    (rabota, 'https://rabota.ua/zapros/python/%D0%BA%D0%B8%D0%B5%D0%B2'),
    (dou, 'https://jobs.dou.ua/vacancies/?category=Python&search=%D0%9A%D0%B8%D0%B5%D0%B2'),
    (djinni, 'https://djinni.co/jobs/keyword-python/kyiv/')
)

city = City.objects.filter(slug='kiev')

jobs, errors = [], []
for func, url in parsers:
    j, e = func(url)
    jobs += j
    errors += e
    
with codecs.open('FROM_4_SITES.json', 'w', 'utf-8') as file:
    json.dump(jobs, file, ensure_ascii=False, indent=4)