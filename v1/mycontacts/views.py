from django.shortcuts import render
from django.http import HttpResponse
import operator

# Create your views here.

def friends(requests):
	return HttpResponse('list of friends')
def family(requests):
	return HttpResponse('list of family')