from django.db import models
from django.utils import timezone

from blog.views.storage import upload_version_2
# Create your models here.
from cestlavie_nataly import settings


class Section(models.Model):
	name = models.CharField(max_length=100, null=False, blank=False, unique=True, verbose_name='Название')
	# image = models.FileField(null=True, verbose_name='Картинка',
	# 						 validators=[FileExtensionValidator(allowed_extensions=['gif','png','jpg', 'jpeg'])])
	avatar = models.ImageField(upload_to='sections', null=True, verbose_name='Картинка')
	created_at = models.DateTimeField(blank=True, null=True, verbose_name='Дата создания')
	updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Дата обновления')

	class Meta:
		db_table = 'section'
		verbose_name = 'Раздел'
		verbose_name_plural = 'Разделы'
		ordering = ['name']

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		# print(self.image)
		try:
			section = Section.objects.get(id=self.id)
			self.updated_at = timezone.now()
			# if section.image != self.image:
			# 	self.image = upload(settings.BUCKET_NAME, self.image)
			super(Section, self).save(*args, **kwargs)
		except Exception:
			now = timezone.now()
			self.created_at = now
			self.updated_at = now
			# self.image_path = upload_version_2(settings.BUCKET_NAME, str(self.image_path))
			super(Section, self).save(*args, **kwargs)
			# section = Section.objects.get(id=self.id)
			# upload_version_2(settings.BUCKET_NAME, str(section.image_path))


class Post(models.Model):
	title = models.CharField(max_length=255, null=False, blank=False, verbose_name='Название')
	annotation = models.CharField(max_length=255, null=True, blank=True, verbose_name='Аннотация')
	avatar = models.ImageField(upload_to='posts', null=True, blank=True, verbose_name='Главная картинка')
	section = models.ForeignKey(Section, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Категория')
	created_at = models.DateTimeField(blank=True, null=True, verbose_name='Дата создания')
	updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Дата обновления')

	class Meta:
		db_table = 'publication'
		verbose_name = 'Публикация'
		verbose_name_plural = 'Публикации'
		ordering = ['created_at']

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		try:
			post = Post.objects.get(id=self.id)
			self.updated_at = timezone.now()
			super(Post, self).save(*args, **kwargs)
		except Exception:
			now = timezone.now()
			self.created_at = now
			self.updated_at = now
			super(Post, self).save(*args, **kwargs)
#
#
# class Content(models.Model):
# 	class ContentType(models.TextChoices):
# 		IMG = 'IMG', _('Картинка')
# 		TEXT = 'TEXT', _('Абзац')
#
# 	type = models.CharField(max_length=5, choices=ContentType.choices, default=ContentType.TEXT)
# 	text = models.TextField(null=True, blank=True, verbose_name='Текст')
# 	image = models.CharField(max_length=200, null=True, blank=True, verbose_name='Картинка')
# 	created_at = models.DateTimeField(blank=True, null=True, verbose_name='Дата создания')
# 	updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Дата обновления')
#
# 	class Meta:
# 		db_table = 'content'
# 		verbose_name = 'Контент'
# 		verbose_name_plural = 'Контенты'
# 		ordering = ['created_at']
