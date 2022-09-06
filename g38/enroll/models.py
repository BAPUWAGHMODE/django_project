from django.db import models

# Create your models here.

class employee(models.Model):
    em_name=models.CharField(max_length=70)
    em_email=models.CharField(max_length=70)
    img=models.ImageField(upload_to='images/')
    pdf=models.FileField(upload_to='pdf/')