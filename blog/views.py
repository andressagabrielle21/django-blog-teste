from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
# As views conectam modelos com templates

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts':posts})
    
