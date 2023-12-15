from django.db import models

# Create your models here.

class Profile(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    date_of_birth = models.DateField(max_length=8)

    def __str__(self):
        return f"{self.full_name}"
