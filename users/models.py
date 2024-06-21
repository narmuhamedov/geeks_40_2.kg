# class Person:
#     def __init__(self, name, age, height):
#         if isinstance(name, str):
#             self.name = name
#         else:
#             raise ValueError("Name must be of type str")
#         if isinstance(age, int):
#             self.age = age
#         else:
#             raise ValueError("Age must be of type int")
#
#         if isinstance(height, float):
#             self.height = height
#         else:
#             raise ValueError("Height must be of type float")
#
#     def __str__(self):
#         return f'{self.name} {self.age} {self.height}'
#
# person_1 = Person(name='John', age='25', height=1.76)
# print(person_1)


from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(User):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    phone_number = models.CharField(max_length=14, default='+996')
    age = models.PositiveIntegerField(default=18, null=True,
                                      validators=[
                                          MaxValueValidator(90),
                                          MinValueValidator(5)
                                      ])
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    club = models.CharField(max_length=20, default='Клуб не определен')


@receiver(post_save, sender=CustomUser)
def set_club(sender, instance, created, **kwargs):
    print('Сигнал успешен пользователь зарегался')
    age = instance.age
    if age < 5:
        instance.club = 'Детский'
    elif age >= 5 and age <= 10:
        instance.club = 'Детский'
    elif age >= 11 and age <= 18:
        instance.club = 'Подростковый'
    elif age >= 18 and age <= 45:
        instance.club = 'Взрослый'
    else:
        instance.club = 'Клуб не определен'
    instance.save()
