from django.db import models

# Create your models here.
class home (models.Model):	
	slide_img = models.ImageField(null=True, blank=True, upload_to ='images/')
	slide_img2 = models.ImageField(null=True, blank=True, upload_to ='images/')
	slide_img3 = models.ImageField(null=True, blank=True, upload_to ='images/')
	bedroom_image = models.ImageField(null=True, blank=True, upload_to="images/")
	bedroom2_image = models.ImageField(null=True, blank=True, upload_to="images/")
	bedroom3_image = models.ImageField(null=True, blank=True, upload_to="images/")
	bedroom4_image = models.ImageField(null=True, blank=True, upload_to="images/")
	gallery_image = models.ImageField(null=True, blank=True, upload_to="images/")
	gallery2_image = models.ImageField(null=True, blank=True, upload_to="images/")
	gallery3_image = models.ImageField(null=True, blank=True, upload_to="images/")
	gallery4_image = models.ImageField(null=True, blank=True, upload_to="images/")
	gallery5_image = models.ImageField(null=True, blank=True, upload_to="images/")

def __str__(self):
    return self.name 



class booked(models.Model):
	departure = models.DateField()
	arrival = models.DateField()
	email = models.CharField( max_length= 300)
	rooms = models.IntegerField()

def __str__(self):
    return self.name 

class contacting(models.Model):
	name= models.CharField( max_length = 1000)
	email = models.CharField(max_length= 300)
	phone = models.CharField(max_length= 300)
	message = models.TextField(max_length= 5000)

def __str__(self):
    return self.name 