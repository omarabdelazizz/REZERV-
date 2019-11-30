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
        fields = ('profile_id','resturant_id',)

class CreateResturantForm(forms.ModelForm):
    class Meta:
        model = Resturant
        fields = ('name','traffic','rate','favourite','Requests','location',)

class CreateRequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('rest_admin_id','RequestTypes','no_of_people',)


class CreateResturantAdminForm(forms.ModelForm):
    class Meta:
        model = ResturantAdmin
        fields = ('traffic','pending_requests')
