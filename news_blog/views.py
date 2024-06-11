from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models, forms


# CRUD CREATE-READ-UPDATE-DELETE

# edit employees
def edit_employee_view(request, id):
    emp_id = get_object_or_404(models.Employees, id=id)
    if request.method == 'POST':
        form = forms.EmployeeForm(request.POST, instance=emp_id)
        form.save()
        return HttpResponse('<h3>Employee updated successfully!</h3>'
                            '<a href="/employees/">Список сотрудников</a>')
    else:
        form = forms.EmployeeForm(instance=emp_id)
    return render(
        request,
        template_name='employees/edit_employee.html',
        context={
            'form': form,
            'emp_id': emp_id
        }
    )


# delete employee
def drop_employee_view(request, id):
    emp_id = get_object_or_404(models.Employees, id=id)
    emp_id.delete()
    return HttpResponse('<h3>Employee delete successfully!</h3>'
                        '<a href="/employees/">Список сотрудников</a>')


# create employee

def create_employee_view(request):
    if request.method == "POST":
        form = forms.EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h3>Employee created successfully!</h3>'
                                '<a href="/employees/">Список сотрудников</a>')
    else:
        form = forms.EmployeeForm()

    return render(
        request,
        template_name='employees/create_emp.html',
        context={'form': form}
    )


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


# drink  tags

def drink_tags_view(request):
    if request.method == 'GET':
        drink_tags = models.Products.objects.filter(tags__name='Вода').order_by('-id')
        return render(
            request,
            template_name='products/drink_tags.html',
            context={'drink_tags': drink_tags}
        )


# all products

def all_products(request):
    if request.method == 'GET':
        products = models.Products.objects.filter().order_by('-id')
        return render(
            request,
            template_name='products/all_products.html',
            context={
                'products': products
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
