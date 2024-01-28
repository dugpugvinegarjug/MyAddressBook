from django.shortcuts import render, redirect
from .models import AddressT
from .forms import AddressForm
from django.contrib import messages

def home(request):
	AllAddresses = AddressT.objects.all
	return render(request, 'home.html', {'AllAddresses' : AllAddresses})

def addressList(request):
	AllAddresses = AddressT.objects.all
	return render(request, 'addressList.html', {'AllAddresses' : AllAddresses})

def addAddress(request):
	if request.method == 'POST':
		form = AddressForm(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request,  ('Address Has Been Added'))
			return redirect(home)
		else:
			messages.success(request, ('Error Processing the Address...'))
			return render(request, 'addAddress.html', {})
	else:
		return render(request, 'addAddress.html')

def edit(request, list_id):
	if request.method == 'POST':
		current_address = AddressT.objects.get(pk=list_id)
		print(f'current address is {current_address}')
		form = AddressForm(request.POST or None, instance=current_address)
		if form.is_valid():
			form.save()
			messages.success(request,  ('Address Has Been Updated'))
			return redirect(home)
		else:
			messages.success(request, ('Error Editing the Address...'))
			return render(request, 'edit.html', {})
	else:
		get_address = AddressT.objects.get(pk=list_id)
		return render(request, 'edit.html', {'get_address': get_address})

def delete(request, list_id):
	if request.method == 'POST':
		current_address = AddressT.objects.get(pk=list_id)
		current_address.delete()
		messages.success(request, ( 'Record was deleted'))
		return redirect('home')
	else:
		messages.success(request, ('Invalid Request'))
		return redirect('home')

