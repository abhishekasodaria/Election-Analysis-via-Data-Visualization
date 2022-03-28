from django.urls import path
from . import views

urlpatterns = [
	path('',views.candidate_info_views,name = 'candidates'),

	path('display_amreli',views.display_amreli,name = 'display_amreli'),
	path('display_lathi',views.display_lathi,name = 'display_lathi'),
	path('display_dhari',views.display_dhari,name = 'display_dhari'),
	
	path('add_amreli',views.add_amreli,name = 'add_amreli'),
	path('add_lathi',views.add_lathi,name = 'add_lathi'),
	path('add_dhari',views.add_dhari,name = 'add_dhari'),
	path('amreli_chart',views.amreli_chart,name = 'amreli_chart'),
	path('amreli_candidate_detail/(?P<pk>\d+)',views.amreli_candidate_detail,name = 'amreli_candidate_detail'),
	
	path('edit_amreli/(?P<pk>\d+)',views.edit_amreli,name = 'edit_amreli'),
	path('edit_lathi/(?P<pk>\d+)',views.edit_lathi,name = 'edit_lathi'),
	path('edit_dhari/(?P<pk>\d+)',views.edit_dhari,name = 'edit_dhari'),
	path('lathi_chart',views.lathi_chart,name = 'lathi_chart'),
	path('lathi_candidate_detail/(?P<pk>\d+)',views.lathi_candidate_detail,name = 'lathi_candidate_detail'),
	path('dhari_chart',views.dhari_chart,name = 'dhari_chart'),
	path('dhari_candidate_detail/(?P<pk>\d+)',views.dhari_candidate_detail,name = 'dhari_candidate_detail'),
	
	path('delete_amreli/(?P<pk>\d+)',views.delete_amreli,name = 'delete_amreli'),
	path('delete_lathi/(?P<pk>\d+)',views.delete_lathi,name = 'delete_lathi'),
	path('delete_dhari/(?P<pk>\d+)',views.delete_dhari,name = 'delete_dhari'),
]