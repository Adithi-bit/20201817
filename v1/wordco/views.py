from django.shortcuts import render
from django.http import HttpResponse
import operator
# Create your views here.

def myhome(requests):
	return render(requests,'wordco/myhome.html',{'name':'Adithi'})
def aboutus(requests):
	return render(requests,'wordco/aboutus.html',{'id':'1602-18-737-003'})
def Myhobbies(requests):
	return HttpResponse('<h1>My Hobbies Pages</h1>') 
