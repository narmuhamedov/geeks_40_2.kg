from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator




class Tag(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Products(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=110)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title















class Employees(models.Model):
    PROGRAMMING_STATUS = (
        ('Full Stack', 'Full Stack'),
        ('Backend Development', 'Backend Development'),
        ('Frontend Development', 'Frontend Development'),
        ('UX-UI Development', 'UX-UI Development'),
    )

    name = models.CharField(max_length=100, verbose_name='Напишите имя сотрудника', null=True)
    email = models.EmailField(default='@gmail.com', verbose_name='Укажите почту сотрудника', null=True)
    image = models.ImageField(upload_to='images/', verbose_name='Загрузите фото', null=True)
    about_emp = models.TextField()
    programming_status = models.CharField(max_length=100, choices=PROGRAMMING_STATUS, verbose_name='Укажите статус программиста', null=True)
    rezume = models.FileField(upload_to='rezume/', verbose_name='Загрузите резюме', null=True, blank=True)
    date_of_birth = models.DateField(verbose_name='Укажите дату рождения', null=True)
    github = models.URLField(verbose_name='Загрузите ваш гит', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}-{self.programming_status}'

    class Meta:
        verbose_name = 'сотрудника'
        verbose_name_plural = 'сотрудники'


class ReviewsEmployees(models.Model):
    reviews_emp = models.ForeignKey(Employees, on_delete=models.CASCADE,
                                    related_name='reviews_employees')
    text = models.TextField()
    stars = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.stars}-{self.reviews_emp}'
