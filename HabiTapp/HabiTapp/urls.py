"""HabiTapp URL Configuration

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
from django.urls import include, path
from Login import views
from django.views.static import serve
from django.conf.urls import url
                          

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage, name='HomePage'),
    path('LoginPage/', views.LoginPage, name='LoginPage'),
    path('SignUp/', views.SignUp, name='SignUp'),
    path('Dashboard/', views.Dashboard, name='Dashboard'),
    path('Dashboard/Date/', views.Date, name="Date"),
    path('Dashboard/WD/', views.WD),
    path('Dashboard/WD2/', views.WD2),
    path('Dashboard/FM/', views.FM),
    path('Dashboard/FM2/', views.FM2),
    path('Dashboard/MUA/', views.MUA),
    url(r'^media/(?P<path>.*)$',serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),                              
]
urlpatterns-urlpatterns+static(settings.MEDIA_URL,document_root-settings.MEDIA_ROOT)

