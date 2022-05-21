from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    pictures = None
    build_year = models.DateTimeField()
    publication_date = models.DateTimeField('Date published')

    def __str__(self):
        return f"Item: {self.name} - Build year: {self.build_year}"
