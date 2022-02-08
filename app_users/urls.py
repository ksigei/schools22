from django.urls import path
from app_users import views


# app_name = 'app_users'
urlpatterns = [
    path('',views.HomeView.as_view(),name='index'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('departments/', views.DepartmentsView.as_view(), name="departments"),
    path('gallery/', views.GalleryView.as_view(), name="gallery"),
    path('activities/', views.ActivitiesView.as_view(), name="activities"),
    path('learn/', views.LearnView.as_view(), name="learn"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('courses/', views.CourseView.as_view(), name="courses"),
    path('events/', views.EventView.as_view(), name="events"),
    path('post_detail/', views.Post_detailView.as_view(), name="post_detail"),
]
