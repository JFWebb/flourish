from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Photo_Pair
from django.views.generic.edit import UpdateView, DeleteView
from .forms import Post_Form, Photo_Form


def signup (request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # automatically login created user
            login(request, user)
            return redirect('posts')
    else:
        error_message = 'Invalid Sign Up - Try Again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def posts_index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})

def posts_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'posts/detail.html', {'post': post})

def add_post(request):
    if request.method == 'POST':
        post_form = Post_Form(request.POST)
        photo_form = Photo_Form(request.POST)
        if all([Post_Form.is_valid(post_form), Photo_Form.is_valid(photo_form)]):
            new_post = post_form.save(commit=False)
            new_photos = photo_form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            new_photos.post = new_post
            new_photos.save()
            return redirect('/posts')
    else:
        post_form = Post_Form()
        photo_form = Photo_Form()
    return render(request, 'main_app/post_form.html', {'post_form': post_form, 'photo_form': photo_form})




class PostUpdate(UpdateView):
    model = Post
    fields = fields = ['time_int', 'time_unit', 'desc']

class PostDelete(DeleteView):
    model = Post
    success_url = '/posts/'