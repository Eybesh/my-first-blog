from django.shortcuts import render
from django.utils import timezone
from blog.models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('published_date')
    print('posts=> '+str(posts))
    return render(request, 'blog/post_list.html', {'posts': posts})
