import json
import os
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from models import *
from django.core.paginator import *
# Create your views here.
def index(request):
	return render(request,'booktest/index.html')



def MyExp(request):
	# ai=int('abc')
	return HttpResponse('hello')


def uploadPic(request):
	return render(request,'booktest/uploadPic.html')	


def uploadHandle(request):
	from django.conf import settings
	pic1 = request.FILES['pic1']
	picName = os.path.join(settings.MEDIA_ROOT,pic1.name)
	# picName = picName.replace('\\','/')
	with open(picName,"wb") as pic:
		for c in pic1.chunks():
			pic.write(c)
	# return HttpResponse(picName)	
	return HttpResponse('<img src="/static/media/%s"/>' %pic1.name)	


def herolist(request,pindex):
	if pindex == '':
		pindex = '1'
	list = HeroInfo.objects.all()
	paginator = Paginator(list,5)
	page = paginator.page(int(pindex))
	context = {'page':page}
	return render(request,'booktest/herolist.html',context)


def area(request):
	return render(request,'booktest/area.html')
def area2(request,id1):
	id1=int(id)
	if id1 == 0:
		data = AreaInfo.objects.filter(parea__isnull=True)
	else:
		data = [{}]
	# print data
	list=[]
	for area in data:
		list.append([area.aid,])
	data1 = {'data':data}
	return JsonResponse(data1)