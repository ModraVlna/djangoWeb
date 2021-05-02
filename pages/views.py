from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request)
	#return HttpResponse("<h1>Hello world</h1>") #string of HTML code
	return render(request, "home.html", {}) #template


def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {}) #template 
	
def about_view(request, *args, **kwargs):
	my_context = {
		"my_text": "This is about us", #dictionary
		"my_number": 123,
		"my_list": [123,424,511],
		"title": "abc this is about us",
		"my_html": "<h1>Hello</h1>"
	}

	return render(request, "about.html", my_context) #template 

def social_view(request, *args, **kwargs):
	return render(request, "social.html", {}) #template 


def chapter_view(request, *args, **kwargs):
	return render(request, "prvnikapitola.html", {}) #template 


def seznam_view(request, *args, **kwargs):
	return render(request, "seznam.html", {}) #template 


def ntice_view(request, *args, **kwargs):
	return render(request, "ntice.html", {}) #template 

def mnozina_view(request, *args, **kwargs):
	return render(request, "mnozina.html", {}) #template 

def cyklus_view(request, *args, **kwargs):
	return render(request, "cyklus.html", {}) #template 

def slovnik_view(request, *args, **kwargs):
	return render(request, "slovnik.html", {}) #template 

def funkce_view(request, *args, **kwargs):
	return render(request, "funkce.html", {}) #template 

def generatory_view(request, *args, **kwargs):
	return render(request, "generatory.html", {}) #template 

def dekoratory_view(request, *args, **kwargs):
	return render(request, "dekoratory.html", {}) #template 

def vyjimky_view(request, *args, **kwargs):
	return render(request, "vyjimky.html", {}) #template 

def soubory_view(request, *args, **kwargs):
	return render(request, "soubory.html", {}) #template 

def tridy_view(request, *args, **kwargs):
	return render(request, "tridy.html", {}) #template 


def zaklady_view(request, *args, **kwargs):
	return render(request, "zaklady.html", {}) #template 

def sablony_view(request, *args, **kwargs):
	return render(request, "sablony.html", {}) #template 

def pohledy_view(request, *args, **kwargs):
	return render(request, "pohledy.html", {}) #template

def bootstrap_view(request, *args, **kwargs):
	return render(request, "bootstrap.html", {}) #template

def prvniprojekt_view(request, *args, **kwargs):
	return render(request, "prvniprojekt.html", {}) #template

def komponenty_view(request, *args, **kwargs):
	return render(request, "komponenty.html", {}) #template

def instalace_view(request, *args, **kwargs):
	return render(request, "instalace.html", {}) #template

def nasazeni_view(request, *args, **kwargs):
	return render(request, "nasazeni.html", {}) #template

def knihovny_view(request, *args, **kwargs):
	return render(request, "knihovny.html", {}) #template





