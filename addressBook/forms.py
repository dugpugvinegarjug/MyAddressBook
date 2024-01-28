from django import forms
from .models import AddressT

class AddressForm(forms.ModelForm):
	class Meta:
		model = AddressT
		fields = ["name", "email" , "phone", "address", "city", "stateID", "countryID", "zipcode", "age"]


