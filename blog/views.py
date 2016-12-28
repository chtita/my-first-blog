#where do I want to get content or whatever from? (other files)
from django.shortcuts import render
from django.utils import timezone
from .models import Post

#how do I want the blogposts to be ordered?
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
