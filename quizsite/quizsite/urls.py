from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', views.add),
    path('sub/', views.sub),
    path('mul/', views.mul),
    path('test/', views.test),
    path('test1/', views.test1),
    path('plus/', views.plus),
    path('addsub/', views.addsub),
    path('radiobuttons/', views.radiobuttons),
    path('selectaddsub/', views.selectaddsub),
    path('addsub/', views.addsub),
    path('mcqintable/', views.mcq),
    path('sessionshow/', views.sessionshow),
    path('sessionadd/', views.sessionadd),
    # path('session/', views.session),
    path('', views.index),

]
