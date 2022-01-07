from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'ID {self.id}: {self.name}'
