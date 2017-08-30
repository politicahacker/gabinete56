from django.db import models
from django.contrib.admin import widgets


# Create your models here.
class StringField(models.TextField):
    def formfield(self, **kwargs):
        kwargs['widget'] = widgets.AdminTextInputWidget
        return super(StringField, self).formfield(**kwargs)

# Create your models here.
class Partido(models.Model):
    sigla =StringField(primary_key=True)
    nome = StringField(blank=True)
    logo = models.ImageField(blank=True, upload_to='partidos')

    def __str__(self):
        return self.sigla

class Politico(models.Model):
    nome = StringField(primary_key=True)
    partido = models.ForeignKey(Partido, blank=True, null=True)

    def __str__(self):
        return self.nome