from django.shortcuts import render, get_object_or_404
from .models import Post


def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=True)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('datetime') != None:
        posts = posts.filter(date=kwargs['datetime'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])
    context = {'posts':posts}
    return render(request, "blog/blog.html", context)


def single_view(request, pid):
    posts = Post.objects.filter(status=True)
    post = get_object_or_404(posts, pk=pid)
    context = {'post':post}
    return render(request, "blog/blog-single.html", context)

def blog_search(request):
    posts = Post.objects.filter(status=True)
    if request.method == "GET":
        if s := request.GET.get("s"):
            posts = posts.filter(content__contains=s)    
    context = {'posts':posts}
    return render(request, "blog/blog.html", context)
