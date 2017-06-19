from django.contrib import admin
from .models import Election, ElectionChoices
# Register your models here.

admin.site.register(Election)
admin.site.register(ElectionChoices)
