from django.db import models
import os
DIRPATH = os.path.dirname(__file__)

class Operatingsystem(models.Model):
	name = models.CharField(max_length=30)
	imagepath = models.FilePathField(path=os.path.join(DIRPATH, '../static/os_images/')) #Fix

class Nat_rules(models.Model):
	name = models.CharField(max_length=30)
	public_port = models.IntegerField()
	internal_port = models.IntegerField()
	#Usikker
	#server = models.ForeignKey(Server)

	class Meta:
		verbose_name="Nat Rule"
		verbose_name_plural = 'Nat Rules'


class Server(models.Model):
	title = models.CharField(max_length=30)
	uid = models.CharField(max_length=30)
	operatingsystem = models.ForeignKey(Operatingsystem)
	memory_size = models.IntegerField() #Fix
	disk_size = models.IntegerField() #Fix
	hardware_virtual_extention = models.BooleanField()
	hardware_virtual_extention_exclusive = models.BooleanField()
	vrde_on = models.BooleanField()
	vrde_port = models.IntegerField()
	nat_rule = models.ForeignKey(Nat_rules)
