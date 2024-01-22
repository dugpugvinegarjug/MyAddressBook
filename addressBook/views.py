from django.shortcuts import render, redirect

def home(request):
	return render(request, 'home.html', {})

def addressList(request):
	return render(request, 'addressList.html', {})

def addAddress(request):
	return render(request, 'addAddress.html', {})
