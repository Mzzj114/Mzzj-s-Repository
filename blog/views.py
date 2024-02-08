import os.path

from django.shortcuts import render, get_object_or_404
from django.utils.safestring import mark_safe

from Web_all_dj.settings import BASE_DIR
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

    # html_path = os.path.join(BASE_DIR, "blog/blogs", post.title, "main.html")

    html_text = mark_safe(post.text)

    # later consider to handle each blog as textFeild and their static files as our static files

    # print(html_text)

    context = {
        "title": post.title,
        "text": html_text,
        "post_date": post.post_date,
    }
    return render(request, "blog/posts.html", context)
