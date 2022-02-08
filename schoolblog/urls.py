from django.contrib import admin
from django.urls import path, include

# added
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('home.urls')),
    path('curriculum/',include('curriculum.urls')),
    path('', include('app_users.urls')),
    path('', include('blog.urls', namespace='blog')),
    path('ckeditor/',include('ckeditor_uploader.urls')),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)