from django.db import models




class Sarees (models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100, default='saree')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='sarees/')  

    def __str__(self):
        return self.name.upper()  # will crash if name is None



