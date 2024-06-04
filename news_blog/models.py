from django.db import models


class Employees(models.Model):

    PROGRAMMING_STATUS = (
        ('Full Stack', 'Full Stack'),
        ('Backend Development', 'Backend Development'),
        ('Frontend Development', 'Frontend Development'),
        ('UX-UI Development', 'UX-UI Development'),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField(default='@gmail.com')
    image = models.ImageField(upload_to='images/')
    about_emp = models.TextField()
    programming_status = models.CharField(max_length=100, choices=PROGRAMMING_STATUS, null=True)
    rezume = models.FileField(upload_to='rezume/')
    date_of_birth = models.DateField()
    github = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}-{self.programming_status}'

    class Meta:
        verbose_name = 'сотрудника'
        verbose_name_plural = 'сотрудники'
