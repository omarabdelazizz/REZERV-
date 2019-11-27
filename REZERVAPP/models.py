from django.db import models


class profile(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=264, unique=True)
    picture = models.CharField(max_length=264, unique=True)
    Email = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.name
        return self.entity
        return self.role

class best(models.Model):
    #best is the favourits
    profile_id = models.ManyToManyField('profile')
    resturant_id = models.ManyToManyField('Resturant')

    def __str__(self):
        return str(self.profile)
        return str(self.Resturant)

class Resturant(models.Model):
    name = models.CharField(max_length=264, unique=True)
    traffic = models.IntegerField()
    rate = models.CharField(max_length=264, null=True , blank=True)
    favourite = models.CharField(max_length=264, null=True , blank=True)
    Requests = models.CharField(max_length=264, null=True , blank=True)
    location = models.CharField(max_length=264, unique=True)

class Request(models.Model):
    rest_admin_id = models.AutoField(primary_key=True)
    time = models.CharField(max_length=264, null=True)
    no_of_people = models.CharField(max_length=264, null=True)
    date = models.CharField(max_length=264, null=True)

class RequestTypes(models.Model):
    Accepted=models.BooleanField(default=False)
    rejected=models.BooleanField(default=True)
    canceled=models.BooleanField(default=False)
    pending =models.BooleanField(default=False)
class ResturantAdmin (models.Model):
    traffic=models.IntegerField()
