"""cestlavie_nataly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path

from blog.views.publications import home, posts, show_post, about, find_posts_by_other_categories, \
	find_posts_by_category_url
from cestlavie_nataly import settings

urlpatterns = [
		path('harniohta/', admin.site.urls),

		path('posts/category/others', find_posts_by_other_categories),
		path('posts/category/<str:url>', find_posts_by_category_url),
		path('posts/<int:id>', show_post),
		path('posts/', posts),

		path('about', about),
		path('', home)
		]

handler404 = 'blog.views.errors.page_not_found_view'
# if settings.DEBUG:
# 	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
