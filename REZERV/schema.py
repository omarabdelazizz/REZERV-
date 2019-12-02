import graphene
import REZERVAPP.schema


class Query(REZERVAPP.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class Mutation(REZERVAPP.schema.Mutation, graphene.ObjectType):
    # This class will inherit from multiple mutation
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
