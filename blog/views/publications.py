from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Section, Post, Content


# Create your views here.
def home(request):
	sections = Section.objects.all()
	posts = Post.objects.all().order_by('-created_at')[:6]
	data = {
			'sections' : sections,
			'publications': posts
			}
	return render(request, 'blog/home.html', data)

# def publications_by_section(request, category_id):


def posts(request):
	post_list = Post.objects.all().order_by('-created_at')
	paginator = Paginator(post_list, 2)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	data = {
			'page_obj': page_obj
			}
	return render(request, 'blog/posts.html', data)


def show_post(request, id):
	post = Post.objects.get(id=id)
	contents = Content.objects.filter(post=post)
	data = {
			'post': post,
			'contents': contents
			}
	return render(request, 'blog/post.html', data)


def about(request):
	return render(request, 'blog/about.html')
