from django.shortcuts import render, get_object_or_404
from .models import Article
# Create your views here.



def detail(request,tag, slug):
    post = get_object_or_404(Article, tag=tag, slug=slug)
    return render(request, 'blog/detail.html', {'post':post})




def list_view(request):
    posts = Article.objects.all()
    return render(request, 'blog/list.html', {'posts':posts})
