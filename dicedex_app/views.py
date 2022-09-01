from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Game
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.functions import Now

# Create your views here.

def home(request):
    return render(request, 'home.html')

@login_required
def library_index(request):
    games = Game.objects.order_by('title')
    return render(request, 'library/index.html', { 'games': games })


# Game
class GameCreate(LoginRequiredMixin, CreateView):
  model = Game
  fields = ['title', 'genre', 'min', 'max', 'length', 'image', 'type', 'owner', 'note', 'link']
  
  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

class GameUpdate(LoginRequiredMixin, UpdateView):
  model = Game
  fields = ['title', 'genre', 'min', 'max', 'length', 'image', 'type', 'owner', 'note', 'link']

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