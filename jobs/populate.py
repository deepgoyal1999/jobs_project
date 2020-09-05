import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jobs.settings')

import django
django.setup()

from recruiter.models import *
from faker import Faker
from random import *
fake=Faker()

def phonenumgen():
    d1=randint(6,9)
    num='' +str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return(num)

def populate1(n):
    for i in range(n):
        fdate=fake.date()
        #fcname=fake.company_name()
        ftitle=fake.random_element(elements=('Project Manager', 'TeamLead', 'Software Engineer'))
        fphonenum=phonenumgen()
        job_record=mumbaijobinfo.objects.get_or_create(date=fdate,title=ftitle,phonenum=fphonenum)

def populate2(n):
    for i in range(n):
        fdate=fake.date()
        #fcname=fake.company_name()
        ftitle=(fake.random_element(elements=('Project Manager', 'TeamLead', 'Software Engineer')))
        fphonenum=phonenumgen()
        job_record=delhijobinfo.objects.get_or_create(date=fdate,title=ftitle,phonenum=fphonenum)

def populate(n):
    for i in range(n):
        fdate=fake.date()
        #fcname=fake.company_name()
        ftitle=(fake.random_element(elements=('Project Manager', 'TeamLead', 'Software Engineer')))
        fphonenum=phonenumgen()
        job_record=hydjobinfo.objects.get_or_create(date=fdate,title=ftitle,phonenum=fphonenum)

populate(20)
populate1(20)
populate2(20)
