from django.core.paginator import Paginator
from django.shortcuts import render

from blog.models import Section, Post, Content


# Create your views here.
def home(request):
	sections = Section.objects.all().filter(post=not None)
	posts = Post.objects.all().order_by('-created_at')[:6]
	posts_without_category_count = Post.objects.filter(section=None).count()
	context = {
			'sections'    : sections,
			'publications': posts,
			'no_category_posts_count': posts_without_category_count
			}
	return render(request, 'blog/home.html', context)


# def publications_by_section(request, category_id):

def find_posts_by_other_categories(request):
	post_list = Post.objects.filter(section=None)
	paginator = Paginator(post_list, 2)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context = {
			'page_obj': page_obj
			}
	return render(request, 'blog/posts.html', context)


def find_posts_by_category_url(request, url):
	section = Section.objects.get(url=url)
	post_list = Post.objects.filter(section__url=url)
	paginator = Paginator(post_list, 2)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context = {
			'section': section,
			'page_obj': page_obj
			}
	return render(request, 'blog/posts.html', context)


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

	def show_last_post_by_section(request_post):
		last_posts_by_section: list = Post.objects.filter(section=request_post.section).order_by('-created_at')[:4]
		last_posts = list(last_posts_by_section)
		if request_post in last_posts:
			last_posts.remove(request_post)
			return last_posts
		return last_posts_by_section[:3]

	post = Post.objects.get(id=id)
	contents = Content.objects.filter(post=post)
	related_by_section_last_posts = show_last_post_by_section(post)

	data = {
			'post': post,
			'related_posts': related_by_section_last_posts,
			'contents': contents
			}
	return render(request, 'blog/post.html', data)


def about(request):
	return render(request, 'blog/about.html')
