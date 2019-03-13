from django.db import models

class MinhasImagens(models.Model):
    name = models.CharField(max_length=150)
    foto = models.ImageField(upload_to='minhasimagens', null=True, blank=True)
    descricao = models.TextField()

    def __str__(self):
        return self.name

