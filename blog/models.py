from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class Article(models.Model):
	STATUS_CHOICES = (
		('draft', 'در حال انتظار'),
		('published', 'منتشر شده'),
		)
	title = models.CharField(max_length = 50)

	slug = models.SlugField(max_length=20,allow_unicode=True)

	body = RichTextUploadingField()

	summary = models.CharField(max_length=300,blank=True,null=True,default='')

	publish = models.DateTimeField(default = timezone.now, verbose_name='انتشار')

	created = models.DateTimeField(auto_now_add = True, verbose_name='ساخت',null=True)

	updated = models.DateTimeField(auto_now = True,verbose_name='آپدیت')

	status = models.CharField(max_length=60, choices = STATUS_CHOICES, default='draft', verbose_name='وضعیت')

	def get_absolute_url(self):

		return reverse("blog:detail", args =[self.slug])
