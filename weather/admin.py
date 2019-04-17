from django.contrib import admin
from .models import City,Continent,Temp_changes_couses,Earthquake_data

admin.site.register(City)
admin.site.register(Continent)
admin.site.register(Temp_changes_couses)
admin.site.register(Earthquake_data)