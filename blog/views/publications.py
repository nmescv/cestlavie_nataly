from django.shortcuts import render


# Create your views here.
def index(request):
	return render(request, 'blog/home.html')


def publications(request):
	return render(request, 'blog/publications.html')


def post(request):
	return render(request, 'blog/post.html')


def about(request):
	return render(request, 'blog/about.html')
