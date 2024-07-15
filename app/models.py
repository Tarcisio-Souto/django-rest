from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)

