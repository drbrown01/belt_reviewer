from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    name       = models.CharField(max_length=255)
    email      = models.CharField(max_length=255)
    password   = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Authors(models.Model):
    title       = models.CharField(max_length=255)
    # author = models.CharField(max_length=255)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title       = models.CharField(max_length=255)
    author      = models.ForeignKey(Authors, related_name="books")
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
class Reviews(models.Model):
    review  = models.TextField(max_length=255)
    rating  = models.IntegerField()
    user    = models.ForeignKey(User, related_name="reviews")
    book   = models.ForeignKey(Book, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
