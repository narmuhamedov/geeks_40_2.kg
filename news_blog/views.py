from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models


# Detail Employees
def employees_detail_view(request, id):
    if request.method == "GET":
        emp_id = get_object_or_404(models.Employees, id=id)
        return render(
            request,
            template_name="employees/employees_detail.html",
            context={
                "emp_id": emp_id
            }
        )


# List Employees

def employees_list_view(request):
    if request.method == 'GET':
        queryset = models.Employees.objects.filter().order_by('-id')
        return render(
            request,
            template_name='employees/employees_list.html',
            context={
                'emp': queryset
            }
        )


def news_blog_view(request):
    if request.method == 'GET':
        return HttpResponse('ВАШ РЕБЕНОК В НАДЕЖНЫХ РУКАХ '
                            'Вы можете быть уверены в безопасности вашего ребенка, '
                            'поскольку наш коллектив состоит из большого числа сотрудников, '
                            'ответственных за создание всех условий для комфортного обучения. '
                            'а наш офис расположен в престижном бизнес-центре "Виктори", '
                            'что обеспечивая надежное и безопасное окружение для работы.')


def about_me_view(request):
    if request.method == 'GET':
        return HttpResponse('Всем привет меня зовут Радомир я backend developer')


def geeks_view(request):
    if request.method == 'GET':
        return HttpResponse('<h1>Привет GEEKS</h1>')
