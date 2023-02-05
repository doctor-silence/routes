from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from cities.forms import HtmlForm, CityForm
from cities.models import City

__all__ = (
    'home', 'CityDetailView', 'CityCreateView', 'CityUpdateView', 'DeleteView'
)


def home(request, pk=None):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():   #Проверяем что форма валидна
            print(form.cleaned_data)  #Получаем нужные данные из формы
            form.save()             #Сохраняем полученные данные
    #if pk:
        #city = City.object.filter(id=pk).first  #Что-бы не получить ошибку Does not Exist используем filter
        #city = get_object_or_404(City, id=pk)

        #context = {'object': city}
        #return render(request, 'cities/detail.html', context)
    form = CityForm()
    qs = City.objects.all()
    context = {'objects_list': qs, 'form': form}
    return render(request, 'cities/home.html', context)

class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'

class CityCreateView(CreateView):   #Добавление города
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:home') # После создания переадресация

class CityUpdateView(UpdateView):   #Изменение
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:home')

class CityDeleteView(DeleteView):
    model = City
    template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities:home')
