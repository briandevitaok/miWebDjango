from django.db import models

class Posteos(models.Model):
    titulo = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='media/', null=False, blank=False)


    def __str__(self):
        return self.titulo
