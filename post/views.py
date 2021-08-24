from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Group

def index(request):
    params = {
        "recent_post": Post.objects.order_by('-created_at')[:5],
        "category" :Category.objects.all(),
    }
    return render(request, 'post/index.html', params)

def detail(request, post_id):
    post_text = get_object_or_404(Post, id=post_id)
    return render(request, 'post/detail.html', {'post_text': post_text})


def reveal(request):
    return render(request, 'post/reveal.js/index.html')   
