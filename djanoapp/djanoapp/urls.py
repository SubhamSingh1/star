"""djanoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',views.hello),
    path('gm/',views.gm),
    path('gn/',views.gn),
    path('index/',views.index),
    path('eveodd/',views.eveodd),
    path('indexdate/',views.indexdate),
    path('mi/',views.mi),
    path('index1/',views.index1),
    path('oppo/', views.oppo),
    path('vivo/', views.vivo),
    path('find/', views.find),
    path('find1/', views.find1),
    path('find2/', views.find2),
    path('index11/', views.index11),
    path('ssession/', views.setsession),
    path('gsession/', views.getsession1),
    path('s/', views.setcookie),
    path('g/', views.getcookie),

]

