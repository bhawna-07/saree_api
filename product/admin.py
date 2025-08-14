from django.contrib import admin
from. models import Sarees

@admin.register(Sarees)
class SareeAdmin(admin.ModelAdmin):
  fields = ["category", "description", "price", "image"]




