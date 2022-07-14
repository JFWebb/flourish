from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView
from .models import Post, Photo_Pair
from .forms import Post_Form
import uuid
import boto3

# session = boto3.Session(profile_name='flourish')
# dev_s3_client = session.client('s3')
S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'flourish-jfw'


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
    if request.user.is_authenticated:
        return redirect('/posts/')
    else:
        return redirect('/accounts/signup/')


def about(request):
    return render(request, 'about.html')

@login_required
def posts_index(request):
    posts = Post.objects.all().order_by('-time_stamp')
    return render(request, 'posts/index.html', {'posts': posts})

@login_required
def posts_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'posts/detail.html', {'post': post})

@login_required
def add_photo(request, post):
    ref_photo = request.FILES.get('ref_url', None)
    art_photo = request.FILES.get('art_url', None)
    if all([ref_photo, art_photo]):
        s3 = boto3.client('s3')
        ref_key = uuid.uuid4().hex[:6] + ref_photo.name[ref_photo.name.rfind('.'):]
        art_key = uuid.uuid4().hex[:6] + art_photo.name[art_photo.name.rfind('.'):]
        try:
            # upload ref photo
            s3.upload_fileobj(ref_photo, BUCKET, ref_key)
            ref_url = f"{S3_BASE_URL}{BUCKET}/{ref_key}"

            # upload art photo
            s3.upload_fileobj(art_photo, BUCKET, art_key)
            art_url = f"{S3_BASE_URL}{BUCKET}/{art_key}"

            # save both photos to Photo_Pair
            photo_pair = Photo_Pair(ref_url=ref_url, art_url=art_url, post = post)
            photo_pair.save()
        except: 
            print('An error occured uploading file to S3')

@login_required          
def add_post(request):
    error_message = ''
    if request.method == 'POST':
        post_form = Post_Form(request.POST)

        if all([Post_Form.is_valid(post_form)]):
            # post model
            new_post = post_form.save(commit=False)
            new_post.user = request.user
            new_post.save()

            # photo model
            add_photo(request, new_post)
            return redirect('/posts/')
    else:
        post_form = Post_Form()
    return render(request, 'main_app/post_form.html', {'post_form': post_form})


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['time_int', 'time_unit', 'desc']


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/posts/'