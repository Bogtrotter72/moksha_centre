from django.core.mail import send_mail
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render, reverse
from taggit.models import Tag

from .forms import CommentForm, EmailPostForm
from .models import Comment, Post


def post_list(request, tag_slug=None):
    object_list = Post.objects.all()

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

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
        'tag': tag,
    }

    return render(request, 'forum/list.html', context)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             published__year=year,
                             published__month=month,
                             published__day=day)

    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    # Retrieve the tags from current post
    post_tags_ids = post.tags.values_list('id', flat=True)

    # Retrieve all posts with matching tags (exluding current post)
    similar_posts = Post.objects.filter(
        tags__in=post_tags_ids).exclude(id=post.id)

    # Annotate with 'same_tags'; order by 'same_tags'; limit to 4 most recently published
    similar_posts = similar_posts.annotate(same_tags=Count(
        'tags')).order_by('-same_tags', '-published')[:4]

    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'similar_posts': similar_posts,
    }
    return render(request, 'forum/detail.html', context)


def post_share(request, post_id):
    # Retrieve post by its id
    post = get_object_or_404(Post, id=post_id)
    sent = False

    # Form submitted
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']}, recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'admin@mokshacentre.ie', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()

    context = {
        'post': post,
        'form': form,
        'sent': sent,
    }
    return render(request, 'forum/share.html', context)
