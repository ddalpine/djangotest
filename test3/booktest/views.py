#coding:utf8
from django.shortcuts import render,redirect
from django.http  import HttpResponse,HttpResponseRedirect
# Create your views here.


def index(request):
	return HttpResponse(request.path)
def detail(request,p1,p2,p3):
	return HttpResponse('year:%s,month:%s,day:%s'%(p1,p2,p3))

def getTest1(request):
	return render(request,'booktest/getTest1.html')
def getTest2(request):
	a1 = request.GET['a']
	b1 = request.GET['b']
	c1 = request.GET['c']
	context = {'a':a1,'b':b1,'c':c1}
	return render(request,'booktest/getTest2.html',context)
def getTest3(request):
	a1 = request.GET.getlist('a')
	context = {'a':a1}
	return render(request,'booktest/getTest3.html',context)

def postTest1(request):
	return render(request,'booktest/postTest1.html')

def postTest2(request):
	uname = request.POST['uname']
	upwd = request.POST['upwd']
	ugender = request.POST.get('ugender')
	uhobby = request.POST.getlist('uhobby')
	context = {'uname':uname,'upwd':upwd,'ugender':ugender,'uhobby':uhobby}
	return render(request,'booktest/postTest2.html',context)	


def cookieTest(request):
	response = HttpResponse()
	cookie = request.COOKIES
	if cookie.has_key('t1'):
		response.write(cookie['t1'])
	# response.set_cookie('t1','abc')
	return response


def redTest1(request):
	# return HttpResponseRedirect('/booktest/redTest2/')
	return redirect('/booktest/redTest2/')
def redTest2(request):
	return HttpResponse('这是转向来的页面')




def session1(request):
	uname = request.session.get('myname','未登录')
	context = {'uname':uname}
	return render(request,'booktest/session1.html',context)


def session2(request):
	return render(request,'booktest/session2.html')
def session3(request):
	# return render(request,'booktest/session2.html')	
	del request.session['myname']
	return redirect('/booktest/session1/')



def session2_handle(request):
	uname = request.POST['uname']
	request.session['myname'] = uname
	request.session.set_expiry(0)
	return redirect('/booktest/session1/')