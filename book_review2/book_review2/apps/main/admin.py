from django.contrib import admin
from .models import User, Book, Authors, Reviews
# Register your models here.
admin.site.register(User),
admin.site.register(Book),
admin.site.register(Authors),
admin.site.register(Reviews)
