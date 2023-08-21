from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('expense', views.add_expense, name='add_expense'),
    path('somewhere', views.somewhere, name='somewhere'),
    path('about', views.about, name='about')
]
