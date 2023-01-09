from django.shortcuts import render
from blog.models import Section, Post


# Create your views here.
def home(request):
	sections = Section.objects.all()
	posts = Post.objects.all().order_by('created_at')[:6]
	data = {
			'sections' : sections,
			'publications': posts
			}
	return render(request, 'blog/home.html', data)


def publications(request):
	return render(request, 'blog/publications.html')


def post(request):
	return render(request, 'blog/post.html')


def about(request):
	return render(request, 'blog/about.html')
