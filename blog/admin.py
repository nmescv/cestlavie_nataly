import os
from pathlib import Path

from django.contrib import admin

from blog.views.storage import upload, delete
from blog.models import Section, Post
from blog.forms import SectionForm


# Register your models here.
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):

	list_display = ('name', 'avatar', 'created_at', 'updated_at')
	fields = ('name', 'avatar')

	# class Meta:
	# 	form = SectionForm
	#
	# def save_model(self, request, obj, form, change):
	# 	if request.method == 'POST':
	# 		print(obj.name)
	# 		print(Path(str(obj.image_path)).resolve())


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

	list_display = ('title', 'annotation', 'avatar', 'section', 'created_at', 'updated_at')
	fields = ('title', 'annotation', 'avatar', 'section')