from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Photo_Pair
from django.views.generic.edit import CreateView, UpdateView, DeleteView


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

class PostCreate(CreateView):
    model = Post
    fields = ['time_int', 'time_unit', 'desc']
    success_url= '/posts/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostUpdate(UpdateView):
    model = Post
    fields = fields = ['time_int', 'time_unit', 'desc']

class PostDelete(DeleteView):
    model = Post
    success_url = '/posts/'