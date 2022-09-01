from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Game
# from django.contrib.auth import login
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.db.models.functions import Now

# Create your views here.

def home(request):
    return render(request, 'home.html')

def library_index(request):
    games = Game.objects.order_by('title')
    return render(request, 'library/index.html', { 'games': games })


# Game
class GameCreate(CreateView):
  model = Game
  fields = ['title', 'genre', 'min', 'max', 'length', 'image', 'type', 'owner', 'note', 'link']
  
#   def form_valid(self, form):
#     form.instance.user = self.request.user  
#     return super().form_valid(form)

class GameUpdate(UpdateView):
  model = Game
  fields = ['title', 'genre', 'min', 'max', 'length', 'image', 'type', 'owner', 'note', 'link']

class GameDelete(DeleteView):
  model = Game
  success_url = '/library/'