from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest


class AgeClubMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            age = int(request.POST.get('age'))
            if age < 5:
                return HttpResponseBadRequest('Вы слишком малы для регистрации клуб')
            elif age >= 5 and age <= 10:
                request.club = 'Детский'
            elif age >= 11 and age <= 18:
                request.club = 'Подростковый'
            elif age > 18 and age <= 45:
                request.club = 'Взрослый'
            else:
                return HttpResponseBadRequest('Вы слишком стар для регистрации в клуб')

        elif request.path == '/register/' and request.method == 'GET':
            setattr(request, 'club', 'Клуб не определен')
