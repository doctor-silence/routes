from django.urls import path

from trains.views import *
from trains.views import TrainUpdateView, TrainDeleteView

urlpatterns = [
    #path('', home, name='home'),
    path('', TrainListView.as_view(), name='home'),
    path('detail/<int:pk>/', TrainDetailView.as_view(), name='detail'),  # Может быть целое число которое поместим в pk
    path('update/<int:pk>/', TrainUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', TrainDeleteView.as_view(), name='delete'),
    path('add/', TrainCreateView.as_view(), name='create'),
]
