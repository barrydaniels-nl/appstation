from django.db import models

# Create your models here.

class Settings(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    default = models.CharField(max_length=100, null=True, blank=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    