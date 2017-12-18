from django.shortcuts import render
from django.http import HttpResponse
from learn.models import hongwai
from learn.models import peoplenum
from datetime import datetime
import pytz  # $ pip install tzlocal
import time
#display data
def home(request):
        string = hongwai.objects.all()
	local_timezone = pytz.timezone("Asia/Taipei") # get pytz timezone
	for str in string:
		local_time = datetime.fromtimestamp(float(str.time), local_timezone)
		TIME=local_time.strftime("%Y-%m-%d %H:%M:%S (%Z)")
	return render(request,'home.html',locals())

#dataset
def add(request):
	a = request.GET['a']
	b = request.GET['b']
	c = request.GET['c']
	unix_timestamp = time.time()
	hongwai.objects.create(idnum=int(a), time=int(unix_timestamp), distance=float(c))
	return HttpResponse(str("successful update"))

#statues
def statues(request):
	people_num = request.GET['people_num']
	indoor_statue = request.GET['indoor_statue']
	f=open('/home/xbs/test/complete1/learn/templates/f.txt','w')
	f.write(people_num+'\n')
	f.write(indoor_statue)
	f.close()
	return HttpResponse(str("successful update"))
#analysis how many population
def display(request):
	into = 0
	outto = 0
	i = 0
	p = 0
	q = 0
	string = hongwai.objects.all()
	for str in string:
		if(str.idnum == 1 and str.distance != 28.554945 and str.distance != 31.409580):	
			p = 1
			time1=int(str.time)
		if(str.idnum == 2 and str.distance != 28.554945  and str.distance != 31.409580 and p == 1 and 1 <= int(str.time) - time1 <= 5):
			into = into +1
			p = 0
		if(str.idnum == 2 and str.distance != 28.554945 and str.distance != 31.409580):
			q=1
			time2=int(str.time)
		if(str.idnum == 1 and str.distance != 28.554945 and str.distance != 31.409580 and q == 1 and 1 <= int(str.time) - time2 <= 5):
			outto = outto +1
			q = 0
	population = into - outto
	f=open('/home/xbs/test/complete1/learn/templates/f.txt','r')
	people_num = f.readline()
	indoor_statue = f.readline()
	f.close
	unix_timestamp = time.time()
	local_timezone = pytz.timezone("Asia/Taipei") # get pytz timezone
	local_time = datetime.fromtimestamp(unix_timestamp, local_timezone)
	TIME=local_time.strftime("%Y-%m-%d %H:%M:%S (%Z)")
	f=open('/home/xbs/test/complete1/learn/templates/display.html','r')
	display_html=f.read()
	html = display_html %(people_num,indoor_statue,TIME)
	return HttpResponse(html)			
	#return render(request,'display.html'% people_num % indoor_statue,locals())

def peoplenum(request):
	into = 0
	outto = 0
	i = 0
	p = 0
	q = 0
	string = hongwai.objects.all()
	for str in string:
		if(str.idnum == 1 and str.distance != 28.554945 and str.distance != 31.409580):	
			p = 1
			time1=int(str.time)
		if(str.idnum == 2 and str.distance != 28.554945 and str.distance != 31.409580 and p == 1 and 1 <= int(str.time) - time1 <= 5):
			into = into +1
			p = 0
		if(str.idnum == 2 and str.distance != 28.554945 and str.distance != 31.409580):
			q=1
			time2=int(str.time)
		if(str.idnum == 1 and str.distance != 28.554945 and str.distance != 31.409580 and q == 1 and 1 <= int(str.time) - time2 <= 10):
			outto = outto +1
			q = 0
	population = into - outto
	if population<0:
		population = 0
	return render(request,'peoplenum.html',locals())

def return_peoplenum(request):
	into = 0
	outto = 0
	i = 0
	p = 0
	q = 0
	string = hongwai.objects.all()
	for str in string:
		if(str.idnum == 1 and str.distance != 28.554945 and str.distance != 31.409580):	
			p = 1
			time1=int(str.time)
		if(str.idnum == 2 and str.distance != 28.554945 and str.distance != 31.409580 and p == 1 and 1 <= int(str.time) - time1 <= 5):
			into = into +1
			p = 0
		if(str.idnum == 2 and str.distance != 28.554945 and str.distance != 31.409580):
			q=1
			time2=int(str.time)
		if(str.idnum == 1 and str.distance != 28.554945 and str.distance != 31.409580 and q == 1 and 1 <= int(str.time) - time2 <= 10):
			outto = outto +1
			q = 0
	people_num = into - outto
	people_num=3
	if people_num<0:
		people_num = 0
	return HttpResponse(people_num)

	
# Create your views here.
