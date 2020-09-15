from django.contrib import admin
from .models import Tag, Parent, Child

admin.site.register((Tag, Parent, Child))
