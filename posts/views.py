from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import *
from .models import *

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostCreateForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
    else:
        form = PostCreateForm()
    return render(request,'posts/create.html',{'form':form})
