"""Weed_Detection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from Weed_Detection import views
from Users import views as v
from admins import views as av
from django.conf.urls.static import static
from  django.conf import settings


urlpatterns = [
    
    path('admin/', admin.site.urls),
    
    #main views path
    path('', views.index , name='index'),
    
    
    #user urls
    path('userhome/' , v.userhome , name='userhome'),
    path('register/', v.userRegister , name='register'),
    path('userlogin/' , v.userlogin , name='userlogin'),
    path('predication/' , v.Predication , name='predication'),
    
    
    #Admin urls
    path('adminhome/' , av.adminhome , name='adminhome'),
    path('viewuser/', av.viewuser , name="viewuser"),
    path('activateuser/' , av.Activate , name='activateuser'),
    path('deleteuser/', av.Deletuser , name="deleteuser"),
    path('adminlogin/' , av.adminlogin , name='adminlogin'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

