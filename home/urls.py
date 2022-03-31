from django.urls import path
from . import views

app_name = 'home'
urlpatterns=[
    path('',views.dept_list,name="dept_list"),
    path('<slug:department>/',views.dept_detail,name="dept_detail"),
]
