from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='authors/', blank=True, null=True)
    biography = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
