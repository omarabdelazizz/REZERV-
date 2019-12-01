from graphene_django.forms.mutation import DjangoModelFormMutation
from django import  forms
from .models import *

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ('name','picture','Email','requests',)

class CreatebestForm(forms.ModelForm):
    class Meta:
        model = best
        fields = ('profileid','resturantid',)

class CreateResturantForm(forms.ModelForm):
    class Meta:
        model = Resturant
        fields = ('name','traffic','rate','favourite','Requests','location',)

class CreateRequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('restadminid','RequestTypes','noofpeople',)


class CreateResturantAdminForm(forms.ModelForm):
    class Meta:
        model = ResturantAdmin
        fields = ('traffic',)
