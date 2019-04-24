from django.forms import ModelForm, TextInput
from .models import City,City1

class CityForm(ModelForm):
    class Meta:
        model = City
        model = City1
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'}),
        } #updates the input class to have the correct Bulma class and placeholder


class CForm(ModelForm):
    class Meta:
        model = City1
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'}),
        } #updates the input class to have the correct Bulma class and placeholder
