from django.urls import path
from home import views


# app_name = 'home'
urlpatterns = [
    path('departments/', views.DepartmentsView.as_view(), name="departments"),
    path('gallery/', views.GalleryView.as_view(), name="gallery"),
    path('activities/', views.ActivitiesView.as_view(), name="activities"),
    # path('blog/', views.BlogView.as_view(), name="blog"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('events/', views.EventsView.as_view(), name="events"),
    path('courses/', views.CoursesView.as_view(), name="courses"),
]