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
    path('blog/', include('blog.urls')),
    path('home/', include('home.urls')),
    path('ckeditor/',include('ckeditor_uploader.urls')),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)