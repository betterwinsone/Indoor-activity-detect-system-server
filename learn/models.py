from __future__ import unicode_literals

from django.db import models

#frered table
class hongwai(models.Model):
	idnum =  models.IntegerField()
	time = models.IntegerField()
	distance = models.FloatField()
	def __unicode__(self):
    
       		 return u'%d %d %f'%(self.idnum,self.time,self.distance)


#current indoor population table
class indooractivity(models.Model):
	labid = models.IntegerField()
	time_now = models.IntegerField()
	p_num = models.IntegerField()
	def __unicode__(self):
    
       		 return u'%d %s %f'%(self.labid,self.time_now,self.p_num)

class peoplenum(models.Model):
	indoor = models.IntegerField()
	outdoor = models.IntegerField()
	p_num = models.IntegerField()
	def __unicode__(self):
    
       		 return u'%d %s %f'%(self.indoor,self.outdoor,self.p_num)


# Create your models here.
