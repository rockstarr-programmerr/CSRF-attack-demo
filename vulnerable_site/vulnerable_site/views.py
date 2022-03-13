from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt

User = get_user_model()


class CustomLoginView(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('home')


def home(request):
    return HttpResponse('<h1>Hello</h1>')


@csrf_exempt
@login_required
def change_email(request):
    if request.method == 'GET':
        return render(request, 'change_email.html')
    elif request.method == 'POST':
        email = request.POST['email']
        request.user.email = email
        request.user.save()
        return redirect('home')
