from django.urls import path, re_path, include
from django_mark_auth_app import views

# template tagging
app_name = 'basic_app'

urlpatterns=[
    re_path(r'^register/', views.register, name="register"),
    re_path(r'^user_login/$', views.user_login, name="user_login"),
]