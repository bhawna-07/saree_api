from django.db import models

class Sarees (models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100, default='saree')
    description = models.TextField(blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='sarees/')  

    def __str__(self):
        return self.name.upper()  


