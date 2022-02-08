from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView

# Create your views here.

class AboutView(TemplateView):
   template_name = 'app_users/about.html'


class DepartmentsView(TemplateView):
    template_name = 'home/departments.html'

class GalleryView(TemplateView):
    template_name = 'home/gallery.html'
  
class ActivitiesView(TemplateView):
    template_name = 'home/activities.html'

class EventsView(TemplateView):
    template_name = 'home/events.html'

class CoursesView(TemplateView):
    template_name = 'home/courses.html'
