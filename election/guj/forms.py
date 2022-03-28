from django import forms
from .models import *
class CandidateForm(forms.ModelForm):
	class Meta:
		model = Candidatedata
		fields = ("Candidate","Party","Votes","Per_Votes")

class AmreliForm(forms.ModelForm):
	class Meta:
		model = Amreli
		fields = ('Candidate','Party','Votes','Per_Votes')

class LathiForm(forms.ModelForm):
	class Meta:
		model = Lathi
		fields = ('Candidate','Party','Votes','Per_Votes')



