from django.db import models
from django.conf import settings
# Create your models here.
#
# def restricted_count(value):
#     if FamilyMember.objects.filter(parent_id = value).count() > 2:
#         raise ValidationError(" Cannot add more than 2 children")

class Tag(models.Model):
    name = models.CharField(max_length = 40)

    def __str__(self):
        return self.name

class Parent(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete= models.CASCADE)
    skills = models.CharField(max_length=40)
    def __str__(self):
        return self.user.username
    
class Child(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fees = models.BooleanField(default=False)
    skills = models.CharField(max_length=40)

    def __str__(self):
        return "Children added " + self.user.username + " to parent " + self.parent.user.username
    