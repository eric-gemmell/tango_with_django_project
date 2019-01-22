from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

	return render(request, "rango/index.html",context=context_dict)

def v2(request):
	return render(request, "rango/v2.html")
