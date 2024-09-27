from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import RegisterForm
# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, 'app/index.html')

class RegisterView(View):
    def get(self, request):
        context={
            'title': 'Register',
            'image_url':'https://i.pinimg.com/originals/21/36/47/21364773a0a5aba924a396b5e86b1951.png'
        }
        return render(request, 'register.html', context)
    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')
        return redirect('register')