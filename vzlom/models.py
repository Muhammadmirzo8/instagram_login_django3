from django.db import models

class Userbek(models.Model): 
    login1 = models.CharField(max_length=500)
    parol2 = models.CharField(max_length=1000) 

    def __str__(self):
        return f"login:{self.login1} va parol:{self.parol2}"
# Create your models here.
