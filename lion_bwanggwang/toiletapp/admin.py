from django.contrib import admin

# Register your models here.
from .models import ToiletApp
from .models import Comment

admin.site.register(ToiletApp)
admin.site.register(Comment)
