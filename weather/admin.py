from django.contrib import admin
from .models import City,Temp_imp_climate,Temp_changes_couses,Earthquake_data,Feedback,City1

admin.site.register(City1)
admin.site.register(City)
admin.site.register(Temp_imp_climate)



class Temp_changes_cousesAdmin(admin.ModelAdmin):
    list_display = ('heading', 'discription',)
    search_fields = ('heading',)
    class Meta:
        model = Earthquake_data
admin.site.register(Temp_changes_couses,Temp_changes_cousesAdmin)




class EarthquakeAdmin(admin.ModelAdmin):
    list_display = ('date', 'location', 'coordinates','deaths','magnitude',)
    list_filter = ('date', 'location',)
    search_fields = ('location',)
    class Meta:
        model = Earthquake_data
admin.site.register(Earthquake_data,EarthquakeAdmin)




class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'msg',)
    list_filter = ('email', 'msg',)
    search_fields = ('email',)
    class Meta:
        model = Feedback
admin.site.register(Feedback,FeedbackAdmin)