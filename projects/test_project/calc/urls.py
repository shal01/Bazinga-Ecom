from django.urls import path
from calc import views

urlpatterns=[
    path('home/',views.home,name='home'),
    path('add/',views.add,name='add')
]