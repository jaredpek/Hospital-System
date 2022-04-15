from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Doctor(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    gender = models.CharField(max_length=20)
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(130)])
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    identitynum = models.CharField(max_length=9)
    medicalpass = models.CharField(max_length=9)
    email = models.EmailField()
    contactnum = models.IntegerField(validators=[MinValueValidator(60000000), MaxValueValidator(99999999)])

    def __str__(self):
        return f"{self.medicalpass}, Dr {self.firstname} {self.lastname}"


class Patient(models.Model):
    salutation = models.CharField(max_length=10)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    gender = models.CharField(max_length=20)
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(130)])
    identitynum = models.CharField(max_length=9)
    email = models.EmailField()
    contactnum = models.IntegerField(validators=[MinValueValidator(60000000), MaxValueValidator(99999999)])
    allergies = models.CharField(max_length=500)
    medhistory = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.salutation} {self.firstname} {self.lastname}"

