from django.shortcuts import render
import operator
from django.http import HttpResponse

# Create your views here.

def home(requests):
	return render(requests,'counting/home.html')

def count(requests):
	mytext=requests.GET['fulltext']
	rev = mytext[::-1]
	conc=mytext+rev
	return render(requests,'counting/count.html',{'mycount':conc})
