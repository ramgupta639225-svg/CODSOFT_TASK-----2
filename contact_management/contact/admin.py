from django.contrib import admin
from rest_framework.pagination import PageNumberPagination

# Register your models here.

from .models import Contact

admin.site.register(Contact)
