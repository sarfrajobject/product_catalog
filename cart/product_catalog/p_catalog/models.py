from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    stock = models.IntegerField()
    image_url = models.CharField(max_length = 2083)
    Description = models.CharField(max_length = 255)


class Registation(models.Model):
	Full_name = models.CharField(max_length=255)
	username = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	phone_number = models.IntegerField()
	

def get_absolute_url(self):
        return reverse('P_datails', kwargs={'pk': self.pk})