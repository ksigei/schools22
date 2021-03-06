# models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# creating model manager
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')


    # Deparmetnts
class Department(models.Model):
    STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    hod = models.CharField(max_length=250, default='HOD')
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    image = models.ImageField(upload_to='featured_image/%Y/%m/%d/', default='no image for this Department')
    body=RichTextUploadingField() #for ckeditor
    
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')

    class Meta:
        ordering = ('-publish',)
    
    def __str__(self):
        return self.title

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.