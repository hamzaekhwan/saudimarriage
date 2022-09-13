from django.db import models

# Create your models here.


class MarriageContract(models.Model):
    male_firstName=models.CharField(max_length=200, null=True, blank=True)
    male_lastName=models.CharField(max_length=200, null=True, blank=True)
    femaleFather_firstName=models.CharField(max_length=200, null=True, blank=True)
    femaleFather_lastName=models.CharField(max_length=200, null=True, blank=True)
    place=models.CharField(max_length=200, null=True, blank=True)
    placeType=models.CharField(max_length=200, null=True, blank=True)
    accept=models.BooleanField(default=False)




class MarriageDate(models.Model):
    male_firstName=models.CharField(max_length=200, null=True, blank=True)
    male_lastName=models.CharField(max_length=200, null=True, blank=True)
    male_phoneNumber=models.CharField(max_length=200, null=True, blank=True)
    femaleFather_firstName=models.CharField(max_length=200, null=True, blank=True)
    femaleFather_lastName=models.CharField(max_length=200, null=True, blank=True)
    weekDay=models.CharField(max_length=200, null=True, blank=True)
    hijriDay=models.CharField(max_length=200, null=True, blank=True)
    hijriMonth=models.CharField(max_length=200, null=True, blank=True)
    hijriYear=models.CharField(max_length=200, null=True, blank=True)
    date=models.DateField(blank=False)
    place=models.CharField(max_length=200, null=True, blank=True)
    placeType=models.CharField(max_length=200, null=True, blank=True)
    location=models.CharField(max_length=200, null=True, blank=True)
    locationUrl=models.URLField(unique=True,max_length=128)
    image=models.ImageField(null=True, blank=True,
                              default='/placeholder.png') 

    accept=models.BooleanField(default=False)                     