from django.urls import path
from MusicApp import views


urlpatterns=[
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('drinks/',views.drinks,name='drinks'),
    path('events/',views.events,name='events'),
    path('blogs/',views.blogs,name='blogs'),
    path('gallery/',views.gallery,name='gallery'),
    path('menu/',views.menu,name='menu'),
    path('rates/',views.rates,name='rates'),
    path('rooms',views.rooms,name='rooms'),

]