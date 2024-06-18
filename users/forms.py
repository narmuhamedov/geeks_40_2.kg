from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models
from django.db.models.signals import post_save
from django.dispatch import receiver

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female')
)


class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'phone_number',
            'age',
            'gender'
        )

    def save(self, commit=True):
        user = super(CustomRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


@receiver(post_save, sender=models.CustomUser)
def set_club(sender, instance, create, **kwargs):
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
