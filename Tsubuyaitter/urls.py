from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

#''/'' now
urlpatterns = [
    path('',TemplateView.as_view(template_name="tsubuyaitter/appex.html"),name='appex'),
    path('signup/',views.signup,name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name="tsubuyaitter/login.html"),name='login'),
    path('home',views.home, name='home'),
    #path('', views.index, name='t_index'),
    path('<int:room_id>/', views.room, name='room'),
    path('resolved/<int:post_id>', views.resolved, name='resolved'),
    path('dalete/<int:post_id>', views.delete_post, name='deletepost'),
]
