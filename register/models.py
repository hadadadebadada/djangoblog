from django.db import models


# Create your models here.
class Address(models.Model):
    email = models.CharField(max_length=120)
    password = models.TextField(blank=True,
                                null=True)  ##plichteingabe felder erzeugen, so ist die plcihteingabe ausgestellt
    address_1 = models.TextField()
    address_2 = models.TextField()
    city = models.TextField()
    state = models.TextField()
    zip_code = models.TextField()
    check_me_out = models.TextField()


class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=120)
    password1 = models.TextField(blank=True, null=True)
    password2 = models.TextField(blank=True, null=True)
