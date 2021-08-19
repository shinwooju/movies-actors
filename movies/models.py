from django.db import models
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ManyToManyField

class Actor(models.Model):
        first_name = models.CharField(max_length=45)
        last_name = models.CharField(max_length=45)
        date_of_birth = models.DateField()

        class Meta:
            db_table = 'actors'
        def __str__(self):
            return self.first_name + self.last_name + str(self.date_of_birth)

class Movie(models.Model):
        title = models.CharField(max_length=45)
        release_date = models.DateField()
        running_time = models.IntegerField()
        actor = models.ManyToManyField(Actor,related_name="movie")

        class Meta:
            db_table = 'movies'
        def __str__(self):
            return self.title
