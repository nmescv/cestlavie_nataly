from django.core.paginator import Paginator
from django.shortcuts import render

from blog.models import Section, Post, Content


# Create your views here.
def home(request):
	sections = Section.objects.all()
	posts = Post.objects.all().order_by('-created_at')[:6]
	data = {
			'sections'    : sections,
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

	def show_last_post_by_section(request_post):
		last_posts_by_section = Post.objects.filter(section=request_post.section).order_by('-created_at')[:4]
		print(last_posts_by_section)
		# if request_post in last_posts_by_section:
		# 	last_posts_by_section.delete(request_post)
		# 	return last_posts_by_section
		# else:
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
