from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
  email = models.CharField(max_length=255, null=True)
  gender = models.CharField(max_length=255, null=True)
  birth_date = models.DateField(null=True)

# Create your models here.
