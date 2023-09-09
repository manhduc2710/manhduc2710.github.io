from django.shortcuts import render
from .forms import RegisterationForm
from .models import Post
from django.http import HttpResponseRedirect

def index(request):
    data = {'post': Post.objects.all()}
    return render(request, 'pages/home.html', data)
def chitiet(request,id):
    post = {'post': Post.objects.get(id=id)}
    return render(request, 'pages/chitiet.html', post)

def register(request):
    form = RegisterationForm()
    if request.method == 'POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            HttpResponseRedirect('/home')
    return render(request, 'pages/register.html', {'form': form})