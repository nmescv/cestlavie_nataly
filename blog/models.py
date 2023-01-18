from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from django.utils.translation import gettext_lazy as _


# Create your models here.


class Section(models.Model):
	name = models.CharField(max_length=100, null=False, blank=False, unique=True, verbose_name='Название')
	url = models.CharField(max_length=100, null=True, blank=False, unique=True, verbose_name='Url для перехода')
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

	# def save(self, *args, **kwargs):
	# 	try:
	# 		Section.objects.get(id=self.id)
	# 		self.updated_at = timezone.now()
	# 		super(Section, self).save(*args, **kwargs)
	# 	except:
	# 		now = timezone.now()
	# 		self.created_at = now
	# 		self.updated_at = now
	# 		super(Section, self).save(*args, **kwargs)


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


class Content(models.Model):
	class ContentType(models.TextChoices):
		IMG = 'IMG', _('Картинка')
		TEXT = 'TEXT', _('Абзац')

	post = models.ForeignKey(Post, null=True, verbose_name='Публикация', on_delete=models.CASCADE)
	type = models.CharField(max_length=5, choices=ContentType.choices, default=ContentType.TEXT,
							verbose_name='Тип контента')
	text = models.TextField(null=True, blank=True, verbose_name='Текст')
	image = models.ImageField(upload_to='contents', null=True, blank=True, verbose_name='Картинка')
	created_at = models.DateTimeField(blank=True, null=True, verbose_name='Дата создания')
	updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Дата обновления')

	class Meta:
		db_table = 'content'
		verbose_name = 'Контент'
		verbose_name_plural = 'Контенты'
		ordering = ['created_at']

	def save(self, *args, **kwargs):
		if self.type == 'IMG' and (self.image == '' or self.image is None):
			raise ValidationError('Т.к. в качестве контента выбрана картинка, то необходимо загрузить файл')
		elif self.type == 'TEXT' and (self.text == '' or self.text is None):
			raise ValidationError('Т.к. в качестве контента выбрана абзац, то необходимо заполнить абзац текстом')
		try:
			Content.objects.get(id=self.id)
			self.updated_at = timezone.now()
			super(Content, self).save(*args, **kwargs)
		except Exception:
			now = timezone.now()
			self.created_at = now
			self.updated_at = now
			super(Content, self).save(*args, **kwargs)
