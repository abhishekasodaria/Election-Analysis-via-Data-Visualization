from django.urls import path
from . import views
urlpatterns = [
	path('',views.compare_info_views),
	path('detail/(?P<pk>\d+)',views.dhari_compare_detail,name = 'dhari_compare_detail'),
	path('display_dhari',views.dhari_compare,name='dhari_compare'),
	path('detail/(?P<pk>\d+)',views.amreli_compare_detail,name = 'amreli_compare_detail'),
	path('display_amreli',views.amreli_compare,name='amreli_compare'),
	path('detail/(?P<pk>\d+)',views.lathi_compare_detail,name = 'lathi_compare_detail'),
	path('display_lathi',views.lathi_compare,name = 'lathi_compare'),
	path('amreli_chart',views.amreli_chart,name = 'amreli_compare_chart'),
	path('dhari_chart',views.dhari_chart,name = 'dhari_compare_chart'),
	path('lathi_chart',views.lathi_chart,name = 'lathi_compare_chart'),
	

]