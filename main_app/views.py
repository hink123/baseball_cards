from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Card, Case
from .forms import OfferForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def cards_index(request):
    cards = Card.objects.filter(user=request.user)
    return render(request, 'cards/index.html', {
        'cards': cards
    })

@login_required
def cards_detail(request, card_id):
    card = Card.objects.get(id=card_id)
    cases_card_doesnt_have = Case.objects.exclude(id__in = card.cases.all().values_list('id'))
    offer_form = OfferForm()
    return render(request, 'cards/detail.html', {
        'card': card,
        'offer_form': offer_form,
        'cases': cases_card_doesnt_have
    })

class CardCreate(LoginRequiredMixin, CreateView):
    model = Card
    fields = ['name', 'age', 'team', 'position', 'season']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CardUpdate(LoginRequiredMixin, UpdateView):
    model = Card
    fields = ['age', 'team', 'position', 'season']

class CardDelete(LoginRequiredMixin, DeleteView):
    model = Card
    success_url = '/cards/'

@login_required
def add_offer(request, card_id):
    form = OfferForm(request.POST)
    if form.is_valid():
        new_offer = form.save(commit=False)
        new_offer.card_id = card_id
        new_offer.save()
    return redirect('detail', card_id=card_id)

class CaseList(LoginRequiredMixin, ListView):
    model = Case

class CaseDetail(LoginRequiredMixin, DetailView):
    model = Case

class CaseCreate(LoginRequiredMixin, CreateView):
    model = Case
    fields = '__all__'

class CaseUpdate(LoginRequiredMixin, UpdateView):
    model = Case
    fields = ['name', 'value']

class CaseDelete(LoginRequiredMixin, DeleteView):
    model = Case
    success_url = '/cases/'

@login_required
def add_assoc(request, card_id, case_id):
    card = Card.objects.get(id=card_id)
    card.cases.add(case_id)
    return redirect('detail', card_id = card_id)

@login_required
def remove_assoc(request, card_id, case_id):
    Card.objects.get(id=card_id).cases.remove(case_id)
    return redirect('detail', card_id=card_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)