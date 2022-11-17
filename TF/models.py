from django.db import models

# Create your models here.

class image_table(models.Model):
    image_title = models.CharField(max_length=50)
    image_class = models.CharField(max_length=20)
    image_path = models.FileField(upload_to="TF/", max_length=300, null=False, default=None)
    