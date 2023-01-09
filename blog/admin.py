import os
from pathlib import Path

from django.contrib import admin

from blog.views.storage import upload, delete
from blog.models import Section
from blog.forms import SectionForm


# Register your models here.
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):

	list_display = ('name', 'image_path', 'created_at', 'updated_at')
	fields = ('name', 'image_path')

	# class Meta:
	# 	form = SectionForm
	#
	# def save_model(self, request, obj, form, change):
	# 	if request.method == 'POST':
	# 		print(obj.name)
	# 		print(Path(str(obj.image_path)).resolve())