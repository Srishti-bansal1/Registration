from django.contrib import admin

# Register your models here.
from .models import Registration

class RegAdmin(admin.ModelAdmin):
    fields = ('name','dob','email','state','city','pin')
    search_fields = ['name']
    list_display = ['id','name','dob','email','state','city','pin']
    list_filter = ['id']

admin.site.register(Registration,RegAdmin)
