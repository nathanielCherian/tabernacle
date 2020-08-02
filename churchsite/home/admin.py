from django.contrib import admin
from .models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    list_filter = ('name', 'email', 'phone')
    search_fields = ('name', 'email', 'phone')