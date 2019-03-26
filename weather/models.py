from django.db import models

class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self): #show the actual city name on the dashboard
        return self.name
    
    class Meta: #show the plural of city as cities instead of citys
        verbose_name_plural = 'cities'


class Continent(models.Model):
    heading = models.CharField(max_length=50)
    image = models.FileField()
    discription = models.TextField(max_length=1000)

    def __str__(self): 
        return self.heading

class Earthquake(models.Model):
    heading = models.CharField(max_length=50)
    image = models.FileField()
    discription = models.TextField(max_length=1000)

    def __str__(self): 
        return self.heading