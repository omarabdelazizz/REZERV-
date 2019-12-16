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
        filter_fields = ['profile_id','resturant_id']
        interfaces = (relay.Node,)

class ResturantNode(DjangoObjectType):
    class Meta:
        model = Resturant
        filter_fields = ['name','traffic','rate','location','requests']
        interfaces = (relay.Node,)

class RequestNode(DjangoObjectType):
    class Meta:
        model = Request
        filter_fields = ['rest_admin_id','no_of_people','RequestTypes']
        interfaces = (relay.Node,)


class ResturantAdminNode(DjangoObjectType):
    class Meta:
        model = ResturantAdmin
        filter_fields = ['traffic','resturantid','name']
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

#best
class bestType (DjangoObjectType):
    class Meta:
        model = best
class CreatebestMutaion(DjangoModelFormMutation):
    #creat object from comment form
    best = graphene.Field(bestType)

    class Meta:
        form_class =CreatebestForm
        input_field_name = 'favourits'
        return_field_name = 'resturant_id'
#Resturant
class ResturantType (DjangoObjectType):
    class Meta:
        model = Resturant
class CreateResturantMutaion(DjangoModelFormMutation):
    #creat object from comment form
    Resturant = graphene.Field(ResturantType)

    class Meta:
        form_class =CreateResturantForm
        input_field_name = 'data'
        return_field_name = 'resturant_name'
#Request
class RequestTypes(DjangoObjectType):
    class Meta:
        model = Request
class CreateRequestMutaion(DjangoModelFormMutation):
    #creat object from comment form
    Request = graphene.Field(RequestTypes)

    class Meta:
        form_class =CreateRequestForm
        input_field_name = 'req'
        return_field_name = 'succed'

#Resturant_Admin
class ResturantAdminTypes(DjangoObjectType):
    class Meta:
        model= ResturantAdmin
class CreateResturantAdminMutation(DjangoModelFormMutation):
    ResturantAdmin = graphene.Field(ResturantAdminTypes)

    class Meta:
        form_class =CreateResturantAdminForm
        input_field_name = 'new'
        return_field_name = 'done'



class Mutation(ObjectType):
    create_best = CreatebestMutaion.Field()
    create_resturant = CreateResturantMutaion.Field()
    create_request = CreateRequestMutaion.Field()
    create_resturantadmin = CreateResturantAdminMutation.Field()
