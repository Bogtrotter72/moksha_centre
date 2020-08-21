from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
from .models import Comment, Post
from taggit.models import Tag


def post_list(request):
    object_list = Post.objects.all()

    # limit posts to 10 per page
    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'page': page,
        'posts': posts,
    }

    return render(request, 'forum/list.html', context)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   published__year=year,
                                   published__month=month,
                                   published__day=day)
    
    context = {
        'post': post,
    }
    return render(request, 'forum/detail.html', context)