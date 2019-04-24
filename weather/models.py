from django.db import models

class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self): #show the actual city name on the dashboard
        return self.name
    
    class Meta: #show the plural of city as cities instead of citys
        verbose_name_plural = 'cities'






class City1(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self): #show the actual city name on the dashboard
        return self.name
    
    class Meta: #show the plural of city as cities instead of citys
        verbose_name_plural = 'cities_1'








class Temp_imp_climate(models.Model):
    heading = models.CharField(max_length=50)
    image = models.FileField()

    def __str__(self): 
        return self.heading

class Temp_changes_couses(models.Model):
    heading = models.CharField(max_length=50)
    discription = models.TextField(max_length=3000)

    def __str__(self): 
        return self.heading

class Earthquake_data(models.Model):
    date = models.DateField()
    location = models.CharField(max_length=50)
    coordinates = models.CharField(max_length=50)
    deaths = models.CharField(max_length=50)
    magnitude = models.CharField(max_length=50)

    def __str__(self): 
        return self.location
    

    
class Feedback(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    msg = models.TextField() 
    def __str__(self): 
        return self.name
