from django import forms 

class item_sell(forms.Form):
    price = forms.FloatField()
    