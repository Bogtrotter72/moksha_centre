from django.core.mail import send_mail
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
from .forms import EmailPostForm
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
            sent=True
    else:
        form = EmailPostForm()
    
    context = {
        'post': post,
        'form': form,
        'sent': sent,
    }
    return render(request, 'forum/share.html', context)