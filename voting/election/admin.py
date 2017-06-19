from django.contrib import admin
from .models import Election, ElectionChoices
# Register your models here.


class ElectionChoicesInline(admin.TabularInline):
    model = ElectionChoices
    extra = 2

class ElectionAdmin(admin.ModelAdmin):


    inlines = [ElectionChoicesInline]
    list_display = ('name', 'startDate')
    list_filter = ['startDate']

    search_fields = ['name']

admin.site.register(Election, ElectionAdmin)

