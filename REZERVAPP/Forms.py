from graphene_django.forms.mutation import DjangoModelFormMutation
from django import  forms
from .models import *

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ('name','picture','Email',)

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
        fields = ('rest_admin_id','time','no_of_people','date',)

class CreateRequestTypesForm(forms.ModelForm):
        class Meta:
            model = RequestTypes
            fields = ('Accepted','rejected','canceled','pending',)

class CreateResturantAdminForm(forms.ModelForm):
    class Meta:
        model = ResturantAdmin
        fields = ('traffic',)
