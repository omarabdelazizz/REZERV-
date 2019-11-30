from django.db import models


class profile(models.Model):
    name = models.CharField(max_length=264, unique=True)
    picture = models.CharField(max_length=264, unique=True)
    Email = models.CharField(max_length=264, unique=True)
    requests = models.ForeignKey('Request',on_delete=models.CASCADE,)

    def __str__(self):
        return self.name + " " + self.Email

class best(models.Model):
    #best is the favourits
    profile_id = models.ManyToManyField('profile')
    resturant_id = models.ForeignKey('Resturant', on_delete=models.CASCADE,)


class Resturant(models.Model):
    name = models.CharField(max_length=264, unique=True)
    traffic = models.IntegerField()
    rate = models.FloatField(default="", editable=False)
    favourite = models.ForeignKey('best', on_delete=models.CASCADE,)
    Requests = models.ForeignKey('Request',on_delete=models.CASCADE,)
    location = models.CharField(max_length=264, unique=True)

class Request(models.Model):
    rest_admin_id = models.AutoField(primary_key=True)
    #time = models.TimeField(default="", editable=False)
    no_of_people = models.IntegerField(default="", editable=False)
    #date = models.DateField(default="", editable=False)
    ACCEPTED = 'AC'
    REJECTED = 'REJ'
    CANCELED = 'CANC'
    PENDING = 'PEND'
    REQUEST_TYPES_CHOICES = [
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'rejected'),
        (CANCELED, 'canceled'),
        (PENDING, 'pending'),
    ]
    RequestTypes = models.CharField(max_length=264,choices=REQUEST_TYPES_CHOICES,default=ACCEPTED)

    def is_upperclass(self):
        return self.RequestTypes in (self.ACCEPTED , self.REJECTED, self.CANCELED, self.PENDING)

class ResturantAdmin (models.Model):
    traffic=models.IntegerField(default="", editable=False)
