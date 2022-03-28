from django.db import models
#from django.contrib.auth import User
# class Taluka(models.Model):
# 	taluka = models.CharField(max_length = 200)

class Candidatedata(models.Model):
	Candidate = models.CharField(max_length=200)
	Party = models.CharField(max_length=200)
	Votes = models.IntegerField()
	Per_Votes = models.CharField(max_length=100)

	def __unicode__(self):
		return u'%s %d' % (self.Candidate, self.Votes)
	# taluka_id  = models.ForeignKey(Taluka,on_delete=models.CASCADE) 	# Create your models here.
class Data(models.Model):
	Candidate = models.CharField(max_length=200)
	Party = models.CharField(max_length=200)
	Votes = models.IntegerField()
	Per_Votes = models.CharField(max_length=100)

	class Meta:

		abstract = True

class Amreli(Data):
	pass
class Lathi(Data):
	pass

class Dhari_compare(Data):
	pass

class Amreli_compare(Data):
	pass

class Lathi_compare(Data):
	pass
		
class Party(models.Model):
	Party = models.CharField(max_length=200)
	Seats_Won = models.CharField(max_length=200)		
	
	
		