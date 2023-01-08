from django.contrib import admin

from blog.views.storage import upload, delete
from blog.models import Section


# Register your models here.
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
	list_display = ('name', 'image', 'created_at', 'updated_at')
	fields = ('name', 'image')
