from django.db import models

# Create your models here.
class Rohildb(models.Model):
    npm = models.IntegerField(null=True)
    nama = models.CharField(max_length=50)
    alamat = models.CharField(max_length=255)
    tetala = models.CharField(max_length=50)
    kelas = models.CharField(max_length=50)
   
    def __str__(self):
       return self.nama