from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return f'ID {self.id}: {self.title}'
