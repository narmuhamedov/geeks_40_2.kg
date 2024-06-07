from django.urls import path
from . import views

urlpatterns = [
    path('all_products/', views.all_products),
    path('drinks/', views.drink_tags_view),



    path('employees/', views.employees_list_view),
    path('employees/<int:id>/', views.employees_detail_view),



    path('news/', views.news_blog_view),
    path('about/', views.about_me_view),
    path('geeks/', views.geeks_view),
]