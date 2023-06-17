from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500

from . import views

urlpatterns = [
@@ -25,6 +25,7 @@
    path('vsjpolls/', include('vsjpolls.urls')),
    path('books/', include('booksapp.urls')),
    path('test', views.test),
    path('session', views.session),

]