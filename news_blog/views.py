from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models, forms
from django.views import generic


# Кнопка поиска
class SearchView(generic.ListView):
    template_name = 'employees/employees_list.html'
    context_object_name = 'emp'
    paginate_by = 5

    def get_queryset(self):
        return models.Employees.objects.filter(name__icontains=self.request.GET.get('q')).order_by('-id')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


# CRUD CREATE-READ-UPDATE-DELETE

# edit employees
class EditEmployeeView(generic.UpdateView):
    template_name = 'employees/edit_employee.html'
    form_class = forms.EmployeeForm
    success_url = '/employees/'

    def get_object(self, **kwargs):
        emp_id = self.kwargs.get('id')
        return get_object_or_404(models.Employees, id=emp_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(EditEmployeeView, self).form_valid(form=form)


# def edit_employee_view(request, id):
#     emp_id = get_object_or_404(models.Employees, id=id)
#     if request.method == 'POST':
#         form = forms.EmployeeForm(request.POST, instance=emp_id)
#         form.save()
#         return HttpResponse('<h3>Employee updated successfully!</h3>'
#                             '<a href="/employees/">Список сотрудников</a>')
#     else:
#         form = forms.EmployeeForm(instance=emp_id)
#     return render(
#         request,
#         template_name='employees/edit_employee.html',
#         context={
#             'form': form,
#             'emp_id': emp_id
#         }
#     )


# delete employee
class DeleteEmployeeView(generic.DeleteView):
    template_name = 'employees/confirm_delete.html'
    success_url = '/employees/'

    def get_object(self, **kwargs):
        emp_id = self.kwargs.get('id')
        return get_object_or_404(models.Employees, id=emp_id)


# def drop_employee_view(request, id):
#     emp_id = get_object_or_404(models.Employees, id=id)
#     emp_id.delete()
#     return HttpResponse('<h3>Employee delete successfully!</h3>'
#                         '<a href="/employees/">Список сотрудников</a>')


# create employee
class CreateEmployeeView(generic.CreateView):
    template_name = 'employees/create_emp.html'
    form_class = forms.EmployeeForm
    success_url = '/employees/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateEmployeeView, self).form_valid(form=form)


# def create_employee_view(request):
#     if request.method == "POST":
#         form = forms.EmployeeForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h3>Employee created successfully!</h3>'
#                                 '<a href="/employees/">Список сотрудников</a>')
#     else:
#         form = forms.EmployeeForm()
#
#     return render(
#         request,
#         template_name='employees/create_emp.html',
#         context={'form': form}
#     )


# Detail Employees
class EmployeeDetailView(generic.DetailView):
    template_name = 'employees/employees_detail.html'
    context_object_name = 'emp_id'

    def get_object(self, **kwargs):
        emp_id = self.kwargs.get('id')
        return get_object_or_404(models.Employees, id=emp_id)


# def employees_detail_view(request, id):
#     if request.method == "GET":
#         emp_id = get_object_or_404(models.Employees, id=id)
#         return render(
#             request,
#             template_name="employees/employees_detail.html",
#             context={
#                 "emp_id": emp_id
#             }
#         )


# List Employees
class EmployeesListView(generic.ListView):
    template_name = 'employees/employees_list.html'
    context_object_name = 'emp'
    model = models.Employees
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quote'] = models.Quote.objects.order_by('-id')
        return context

    # Если только 1 контент на 1 странице
    # def get_queryset(self):
    #     return self.model.objects.filter().order_by('-id')


# def employees_list_view(request):
#     if request.method == 'GET':
#         queryset = models.Employees.objects.filter().order_by('-id')
#         quoie = models.Quite.objects.filter().order_by('-id')
#         return render(
#             request,
#             template_name='employees/employees_list.html',
#             context={
#                 'emp': queryset,
#             }
#         )


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
