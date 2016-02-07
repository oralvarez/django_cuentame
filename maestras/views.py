from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	n = 1
	z = 0
	import pdb; pdb.set_trace()
	a = n/z
	
	HttpResponse("a = " + a)
