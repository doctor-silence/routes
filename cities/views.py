from django.shortcuts import render, get_object_or_404

from cities.models import City

__all__ = (
    'home',
)


def home(request, pk=None):
    if pk:
        #city = City.object.filter(id=pk).first  #Что-бы не получить ошибку Does not Exist используем filter
        city = get_object_or_404(City, id=pk)

        context = {'object': city}
        return render(request, 'cities/detail.html', context)
    qs = City.objects.all()
    context = {'objects_list': qs}
    return render(request, 'cities/home.html', context)
