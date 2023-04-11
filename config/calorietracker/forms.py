from django import forms
from .models import *


class selectfoodForm(forms.ModelForm):

    class Meta:
        model = Selectfooditem
        fields = "__all__"

    # filtering fooditem selection to user's food items
    def __init__(self, user, *args, **kwargs):
        super(selectfoodForm, self).__init__(*args, **kwargs)
        self.fields['name'].queryset = Fooditem.objects.filter(person=user)
        self.fields['name'].widget.attrs['class'] = 'form-control  '
        self.fields['category'].widget.attrs['class'] = 'form-control '
        self.fields['quantity'].widget.attrs['class'] = 'form-control '
        self.fields['person'].widget.attrs['class'] = 'form-control'


class fooditemcreate(forms.ModelForm):

    class Meta:
        model = Fooditem
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(fooditemcreate, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class']='form-control  '
        self.fields['calorie'].widget.attrs['class']='form-control '
        self.fields['carbs'].widget.attrs['class']='form-control '
        self.fields['protein'].widget.attrs['class']='form-control '
        self.fields['fat'].widget.attrs['class']='form-control '
        self.fields['person'].widget.attrs['class']='form-control'