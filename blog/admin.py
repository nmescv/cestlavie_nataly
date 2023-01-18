import os
from pathlib import Path

from django.contrib import admin

from blog.views.storage import upload, delete
from blog.models import Section, Post, Content
from blog.forms import SectionForm


# Register your models here.
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):

	list_display = ('id', 'name', 'url', 'avatar', 'created_at', 'updated_at')
	fields = ('name', 'avatar', 'url')

	# class Meta:
	# 	form = SectionForm
	#
	# def save_model(self, request, obj, form, change):
	# 	if request.method == 'POST':
	# 		print(obj.name)
	# 		print(Path(str(obj.image_path)).resolve())


class ContentAdmin(admin.TabularInline):
	model = Content
	fk_name = 'post'
	fields = ('type', 'text', 'image')
	readonly_fields = ('created_at', 'updated_at')
	extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

	list_display = ('id', 'title', 'annotation', 'avatar', 'section', 'created_at', 'updated_at')
	fields = ('title', 'annotation', 'avatar', 'section')

	inlines = [
			ContentAdmin
			]