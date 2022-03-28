from django.contrib import admin
from guj.models import *
from import_export.admin import ImportExportModelAdmin
@admin.register(Candidatedata)
@admin.register(Amreli,Lathi)
@admin.register(Party)
@admin.register(Amreli_compare,Lathi_compare,Dhari_compare)
		
class ViewAdmin(ImportExportModelAdmin):
	pass
# Register your models here.
