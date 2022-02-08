from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import (TemplateView, DetailView,
                                    ListView, CreateView,
                                    UpdateView,DeleteView,FormView,)
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import Post








def post_list(request):
    posts = Post.published.all()
    
    paginator = Paginator(posts, 10) # 10 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
        
    return render(request,'post_list.html',{'posts':posts, page:'pages'})

def post_detail(request, post):
    post=get_object_or_404(Post,slug=post,status='published')
    return render(request, 'blog/post_detail.html',{'post':post})

