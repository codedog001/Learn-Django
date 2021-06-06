from django.forms import ModelForm
from .models import Order


class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__' #Form with all of the fields present in Order model
		# fields = ['customer', 'product'] - Create form with specific fields


