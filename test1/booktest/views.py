#coding:utf8
from django.shortcuts import render
# from django.template import RequestContext,loader
# Create your views here.
from django.http import *
from .models import *



def index(request):
	# temp = loader.get_template('booktest/index.html')
	# return HttpResponse(temp.render())
	booklist = BookInfo.objects.all()
	# for b in booklist:
	# 	print b
	context = {'title':booklist}
	return render(request,'booktest/index.html',context)

# def detail(request,id):
# 	return HttpResponse("detail%s"%id)
def show(request,id):
	book = BookInfo.objects.get(pk=id)
	herolist=book.heroinfo_set.all()
	context = {'list':herolist}
	return render(request,'booktest/show.html', context)