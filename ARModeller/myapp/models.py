from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.


def mypath_2(instance,filename):
	return "Input_{}/image_{}".format(instance.item.id,filename)

class RecievingFromApp():
	input =  ArrayField(
            models.CharField(max_length=200, blank=True))

class Item(models.Model):
	title=models.CharField(max_length=255,null=True,blank=True)
	model_status=models.BooleanField(default=False)
	model_path=models.CharField(max_length=255,null=True,blank=True)

	def __str__(self):
		return str(self.title)+"_"+str(self.id)


class Images(models.Model):
	item=models.ForeignKey(Item,on_delete=models.CASCADE)
	image=models.ImageField(upload_to=mypath_2)

	def __str__(self):
		return "image_"+str(self.id)+"_"+str(self.item.id)