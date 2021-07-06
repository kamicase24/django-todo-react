from django.db import models

class ToDo(models.Model):
    title = models.CharField(verbose_name='Titulo', max_length=120)
    description = models.TextField(verbose_name='Descripción')
    completed = models.BooleanField(verbose_name='Completado', default=False)

    def __str__(self):
        return self.title