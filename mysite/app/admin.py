from django.contrib import admin
from .models import Parameter

class ParameterAdmin(admin.ModelAdmin):
    list_display = ('time', 'comp_number', 'hour_meter')

admin.site.register(Parameter, ParameterAdmin)