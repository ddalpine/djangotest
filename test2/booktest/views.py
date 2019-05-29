#coding:utf8
from django.shortcuts import render
from models import *
from django.db.models import Max,F,Q

# Create your views here.

def index(request):
	# list = BookInfo.books1.filter(heroinfo__hcontent__contains='六')
	# list = BookInfo.books1.filter(pk__lte=3)
	# list = BookInfo.books1.aggregate(Max('id'))
	# Max1 = BookInfo.books1.aggregate(Max('bpub_date'))
	# list = BookInfo.books1.filter(bread__gt=F('bcomment'))
	list = BookInfo.books1.filter(Q(pk__lt=4) | Q(btitle__contains='1'))
	context = {'list':list
				# ,'Max1':Max1
				}
	return render(request,'booktest/index.html',context)