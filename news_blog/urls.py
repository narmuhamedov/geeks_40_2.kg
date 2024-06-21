from django.urls import path
from . import views

urlpatterns = [
    path('all_products/', views.all_products),
    path('drinks/', views.drink_tags_view),



    path('', views.EmployeesListView.as_view(), name='employees_aaa'),
    path('employees/<int:id>/', views.EmployeeDetailView.as_view()),
    path('employees/<int:id>/delete/', views.DeleteEmployeeView.as_view()),
    path('employees/<int:id>/update/', views.EditEmployeeView.as_view()),
    path('create_employee/', views.CreateEmployeeView.as_view()),
    path('search/', views.SearchView.as_view(), name='search'),



    path('news/', views.news_blog_view),
    path('about/', views.about_me_view),
    path('geeks/', views.geeks_view),
]