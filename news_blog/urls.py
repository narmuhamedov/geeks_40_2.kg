from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.news_blog_view),
    path('about/', views.about_me_view),
    path('geeks/', views.geeks_view),
]