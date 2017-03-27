from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def suma(request, num1, num2):
	suma = int(num1) + int(num2)
	return HttpResponse(num1 + " + " + num2 + " = " + str(suma))

def resta(request, num1, num2):
	resta = int(num1) - int(num2)
	return HttpResponse(num1 + " - " + num2 + " = " + str(resta))

def mult(request, num1, num2):
	mult = int(num1) * int(num2)
	return HttpResponse(num1 + " x " + num2 + " = " + str(mult))

def div(request, num1, num2):
	try:
		div = int(num1) / int(num2)
		return HttpResponse(num1 + " / " + num2 + " = " + str(div))
	except ZeroDivisionError:
		return HttpResponse("No se puede dividir entre 0")

def error(request):
	return HttpResponse("404 Not Found")