from django.shortcuts import render, redirect
from .models import Posts, likePost, CommentPost
from .forms import PostForm, CommentForm
from django.contrib.auth.models import User



# Create your views here.


def home_page(request):
    # profiles, search_query = searchProfiles(request)
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    post = Posts.objects.filter(
        post_user__name__icontains=search_query).order_by(
        '-post_created')
    context = {'post': post, 'search_query': search_query}
    return render(request, 'instaapp/home.html', context)

def create_post(request):
    post = request.user.profile
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.post_user = post
            user.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'instaapp/create_post.html', context)

def update_post(request, pk):
    posts = Posts.objects.get(id=pk)
    form = PostForm(instance=posts)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=posts)
        if request.user.profile == posts.post_user:
            if form.is_valid():
                form.save()
            return redirect('home')
        else:
            print('not valid user')
    context = {'form': form}
    return render(request, 'instaapp/create_post.html', context)

def delete_post(request, pk):
    post = Posts.objects.get(id=pk)
    if request.method == 'POST':
      if request.user.profile == post.post_user:
            post.delete()
            return redirect('home')
    return render(request, 'instaapp/delete_post.html')

def post_likes(request, pk):
    user = request.user.profile
    post = Posts.objects.get(id=pk)
    current_likes = post.post_likes
    liked = likePost.objects.filter(user=user, post=post)
    if not liked.exists():
        liked = likePost.objects.create(user=user, post=post)
        current_likes = current_likes + 1
    else:
        liked = likePost.objects.filter(user=user, post=post).delete()
        current_likes = current_likes - 1
    post.post_likes = current_likes
    post.save()
    return redirect('home')

def user_post(request, pk):
    posts = Posts.objects.get(id=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        comment = form.save(commit=False)
        comment.posts = posts
        comment.owner = request.user.profile

        comment.save()
        return redirect('home')

    context = {'posts': posts, 'form': form}
    return render(request, 'instaapp/single_post.html', context)

def delete_comment(request, pk):
    comment = CommentPost.objects.get(id=pk)
    if comment.owner.owner == request.user.profile:
        comment.delete()
        return redirect('home')
    return render(request, 'instaapp/home')

