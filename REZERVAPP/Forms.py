from graphene_django.forms.mutation import DjangoModelFormMutation
from django import  forms
from .models import *

class CreatebestForm(forms.ModelForm):
    class Meta:
        model = best
        fields = ('profile_name','resturant_name',)
class CreateResturantForm(forms.ModelForm):
    class Meta:
        model = Resturant
        fields = ('name','location',)

class CreateRequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('no_of_people','RequestTypes',)

class CreateResturantAdminForm(forms.ModelForm):
    class Meta:
        model = ResturantAdmin
        fields = ('name','resturantid',)

class CreateprofileForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ('name','Email',)
