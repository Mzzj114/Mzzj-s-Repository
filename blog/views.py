from django.shortcuts import render, get_object_or_404
from django.utils.safestring import mark_safe

from .models import postThing


# Create your views here.

def index(request):
    all_posts = postThing.objects.order_by("post_date")
    context = {
        "all_posts": all_posts,
    }
    return render(request, "blog/index.html", context)


def posts(request, posttitle):
    post = get_object_or_404(postThing, title=posttitle)

    # security issue: here need extra code to ensure that post.text is safe
    # 注意注入攻击, 考虑外部库 bleach
    html_text = mark_safe(post.text)

    context = {
        "title": post.title,
        "text": html_text,
        "post_date": post.post_date,
    }
    return render(request, "blog/posts.html", context)
