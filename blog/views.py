from django.shortcuts import render

# Create your views here.
from django.utils import timezone

from blog.models import Post


def post_list(request):
    posts= Post.objects.all()
    filtered_posts = Post.objects.filter(published_date__lte=timezone.now())
    return render(request, 'blog/post_list.html', {'posts': posts, 'posts_all': filtered_posts})
