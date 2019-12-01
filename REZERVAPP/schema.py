import graphene
from graphene_django.types import DjangoObjectType
from REZERVAPP.models import *
from graphene_django.filter import DjangoFilterConnectionField
from graphene import relay, ObjectType
from .Forms import *

class profileNode(DjangoObjectType):
    class Meta:
        model = profile
        filter_fields = ['name','picture','Email','requests']
        interfaces = (relay.Node,)
        # fields = ('id', 'first_name', 'email')

class bestNode(DjangoObjectType):
    class Meta:
        model = best
        filter_fields = ['profileid','resturantid']
        interfaces = (relay.Node,)

class ResturantNode(DjangoObjectType):
    class Meta:
        model = Resturant
        filter_fields = ['name','traffic','rate','favourite','Requests','location']
        interfaces = (relay.Node,)

class RequestNode(DjangoObjectType):
    class Meta:
        model = Request
        filter_fields = ['restadminid','noofpeople','RequestTypes']
        interfaces = (relay.Node,)


class ResturantAdminNode(DjangoObjectType):
    class Meta:
        model = ResturantAdmin
        filter_fields = ['traffic']
        interfaces = (relay.Node,)


class Query(ObjectType):
    all_profiles = DjangoFilterConnectionField(profileNode)
    all_best = DjangoFilterConnectionField(bestNode)
    all_resturants = DjangoFilterConnectionField(ResturantNode)
    all_requests = DjangoFilterConnectionField(RequestNode)
    all_resturantadmins = DjangoFilterConnectionField(ResturantAdminNode)

    get_profiles = relay.Node.Field(profileNode)
    get_best = relay.Node.Field(bestNode)
    get_resturants = relay.Node.Field(ResturantNode)
    get_requests = relay.Node.Field(RequestNode)
    get_resturantAdmins = relay.Node.Field(ResturantAdminNode)

#profile
class profileType (DjangoObjectType):
    class Meta:
        model = profile
class CreateprofilesMutaion(DjangoModelFormMutation):
    #creat object from comment form
    profile = graphene.Field(profileType)

    class Meta:
        form_class =CreateProfileForm
        input_field_name = 'name','picture','Email','requests'
        return_field_name = 'name','picture','Email','requests'

#best
class bestType (DjangoObjectType):
    class Meta:
        model = best
class CreatebestMutaion(DjangoModelFormMutation):
    #creat object from comment form
    best = graphene.Field(bestType)

    class Meta:
        form_class =CreatebestForm
        input_field_name = 'profileid','resturantid'
        return_field_name = 'profileid','resturantid'

#Resturant
class ResturantType (DjangoObjectType):
    class Meta:
        model = Resturant
class CreateResturantsMutaion(DjangoModelFormMutation):
    #creat object from comment form
    Resturant = graphene.Field(ResturantType)

    class Meta:
        form_class =CreateResturantForm
        input_field_name = 'name','traffic','rate','favourite','Requests','location'
        return_field_name = 'name','traffic','rate','favourite','Requests','location'

#Request
class RequestsType (DjangoObjectType):
    class Meta:
        model = Request
class CreateRequestMutaion(DjangoModelFormMutation):
    #creat object from comment form
    Request = graphene.Field(RequestsType)

    class Meta:
        form_class =CreateRequestForm
        input_field_name = 'restadminid','RequestTypes','noofpeople'
        return_field_name = 'restadminid','RequestTypes','noofpeople'


#ResturantAdmin
class ResturantAdminType (DjangoObjectType):
    class Meta:
        model = ResturantAdmin
class CreateResturantAdminMutaion(DjangoModelFormMutation):
    #creat object from comment form
    ResturantAdmins = graphene.Field(ResturantAdminType)

    class Meta:
        form_class =CreateResturantAdminForm
        input_field_name = 'traffic'
        return_field_name = 'traffic'


class Mutation(ObjectType):
    create_profile = CreateprofilesMutaion.Field()
    create_best = CreatebestMutaion.Field()
    create_Resturant = CreateResturantsMutaion.Field()
    create_Request = CreateRequestMutaion.Field()
    create_ResturantAdmin = CreateResturantAdminMutaion.Field()
