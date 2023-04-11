from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta():
        model = CustomUser
        fields = ['username','password1','password2','calorielimit']


    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder']='Username...'
        self.fields['username'].widget.attrs['class']='form-control radius'
        self.fields['password1'].widget.attrs['placeholder']='Password...'
        self.fields['password1'].widget.attrs['class']='form-control radius'
        self.fields['password2'].widget.attrs['placeholder']='Password Confirmation...'
        self.fields['password2'].widget.attrs['class']='form-control radius'
        self.fields['calorielimit'].widget.attrs['placeholder']='Daily Calorielimit...'
        self.fields['calorielimit'].widget.attrs['class']='form-control radius'

        for fieldname in ['username','password1','password2','calorielimit'] :
            self.fields[fieldname].help_text = None
            self.fields[fieldname].label = ""

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

# class Profile(forms.Form):
#     height = forms.IntegerField
#     weight = forms.IntegerField

#     class Meta():
#         model=CustomUser
#         fields = ['username','calorielimit']
#         fields.extend(['height','weight'])



#     def __init__(self, *args, **kwargs):
#         super(Profile,self).__init__(*args, **kwargs)
#         self.fields['height'] = forms.IntegerField()
#         self.fields['weight'] = forms.IntegerField()