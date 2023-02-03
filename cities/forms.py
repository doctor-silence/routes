from django import forms

from cities.models import City


class HtmlForm(forms.Form):
    name = forms.CharField(label='Город')

class CityForm(forms.ModelForm):    # Проверка соблюдения уникальности
    name = forms.CharField(label='Город', widget=forms.TextInput(attrs={  #Изменение формы
        'class': 'form-control',
        'placeholder': 'Введите название города'
    }))     #


    class Meta:                     # Поля которые отображаем
        model = City
        fields = ('name',)