from django.contrib import admin
from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Article

class ArticleAdminForm(forms.ModelForm):
    body  = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Article
        fields = '__all__'
class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm

admin.site.register(Article, ArticleAdmin)
