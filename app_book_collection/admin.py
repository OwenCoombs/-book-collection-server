from django.contrib import admin
from app_book_collection.models import *

class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)