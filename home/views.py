from django.shortcuts import render, get_object_or_404
from django.views.generic import (TemplateView, DetailView,
                                    ListView, CreateView,
                                    UpdateView,DeleteView,FormView,)
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import Department

def dept_list(request):
    departments = Department.published.all()
    
    paginator = Paginator(departments, 10) # 10 departments in each page
    page = request.GET.get('page')
    try:
        departments = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        departments = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        departments = paginator.page(paginator.num_pages)
        
    return render(request,'home/dept_list.html',{'departments':departments, page:'pages'})

def dept_detail(request, department):
    department=get_object_or_404(Department,slug=department,status='published')
    return render(request, 'home/dept_detail.html',{'department':department})
