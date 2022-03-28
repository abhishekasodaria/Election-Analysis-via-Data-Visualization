"""election URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from guj import views
urlpatterns = [
	path('aa/',views.show),
	path('ab/',include('guj.urls')),
    path('ef/',include('guj.compareurls')),
    #path('charts/',views.chart),
    #path('add_form/<str:cls>',views.add_data,name = 'add_form'),
    #path('added_data/',views.added_data),
    #path('(?P<pk>\d+)',views.delete_data,name = '_data'),
    path('admin/', admin.site.urls),
    path('party/',views.party_chart),
    path('pchart/',views.win_chart)
]
