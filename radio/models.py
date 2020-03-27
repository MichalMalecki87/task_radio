from django.db import models

# Create your models here.


class Artists(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Hits(models.Model):
    artist_id = models.ForeignKey(Artists, on_delete=models.DO_NOTHING, related_name='artist')
    title = models.CharField(max_length=100)
    title_url = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
