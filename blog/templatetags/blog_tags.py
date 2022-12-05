from unicodedata import category
from django import template
from ..models import Post, Category

register = template.Library()


@register.inclusion_tag('blog/blog-posts.html')
def recent_posts():
    posts = Post.objects.filter(status=1).order_by('-created_date')[:3]
    context = {'posts':posts}
    return context


@register.inclusion_tag('blog/blog-categories.html')
def post_categories():
    posts = Post.objects.filter(status=True)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    context = {'categories':cat_dict}
    return context
