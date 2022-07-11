from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

class Post:
    def __init__(self, timeint, timeunit, timestamp, description, user):
        self.timeint = timeint,
        self.timeunit = timeunit,
        self.timestamp = timestamp,
        self.description = description,
        self.user = user

posts = [
    Post(3, 'minute', '12/12/2121 5:00pm', 'quick hands practice', 'jfwebb'),
    Post(2, 'minute', '01/04/2006 4:00pm', 'eyes practice', 'msteele')
]

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
    return HttpResponse('<h1>Posts Here /ᐠ｡‸｡ᐟ\ﾉ</h1>')