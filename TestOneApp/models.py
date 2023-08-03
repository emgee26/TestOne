from django.db import models


class SampleDataModel(models.Model):
    Id = models.BigAutoField(primary_key=True, null=False)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    DateOfBirth = models.DateField()
    Occupation = models.CharField(max_length=150)
    Email = models.EmailField(unique=True)
    MobileNumber = models.CharField(max_length=50, unique=True)
    Created = models.DateTimeField(auto_now_add=True)
    Modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.Id)
