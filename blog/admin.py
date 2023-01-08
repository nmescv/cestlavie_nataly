import os

from django.contrib import admin

from blog.views.storage import upload, delete
from blog.models import Section


# Register your models here.
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
	list_display = ('name', 'image_path', 'created_at', 'updated_at')
	fields = ('name', 'image_path')

	# def save_model(self, request, obj, form, change):
	# 	print(obj.name)
	# 	print(os.path.splitext(str(obj.image_path)))