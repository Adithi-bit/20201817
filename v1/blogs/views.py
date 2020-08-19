from django.shortcuts import render
from django.http import HttpResponse
import operator

# Create your views here.

def drinks(requests):
	return HttpResponse('Drink water!!')
def foods(requests):
	return HttpResponse('Eat healthy food')