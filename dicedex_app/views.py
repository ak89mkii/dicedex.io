from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Game
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.functions import Now
from django.contrib.auth.models import Group


# Create your views here.

def home(request):
    return render(request, 'home.html')

@login_required
def library_index_01(request):
    games = Game.objects.filter(group=1).order_by('title')
    context = 1
    return render(request, 'library/index.html', { 'games' : games, 'context' : context })

@login_required
def library_index_02(request):
    games = Game.objects.filter(group=2).order_by('title')
    context = 2
    return render(request, 'library/index.html', { 'games' : games, 'context' : context })


# Game
class GameCreate(LoginRequiredMixin, CreateView):
  model = Game
  fields = ['title', 'genre', 'min', 'max', 'length', 'image', 'type', 'group', 'note', 'link']
  
  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

class GameUpdate(LoginRequiredMixin, UpdateView):
  model = Game
  fields = ['title', 'genre', 'min', 'max', 'length', 'image', 'type', 'group', 'note', 'link']

class GameDelete(LoginRequiredMixin, DeleteView):
  model = Game
  success_url = '/library/'


# Signup
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('library')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)