from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Card
from .forms import OfferForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cards_index(request):
    cards = Card.objects.all()
    return render(request, 'cards/index.html', {
        'cards': cards
    })

def cards_detail(request, card_id):
    card = Card.objects.get(id=card_id)
    offer_form = OfferForm()
    return render(request, 'cards/detail.html', {
        'card': card,
        'offer_form': offer_form
    })

class CardCreate(CreateView):
    model = Card
    fields = '__all__'

class CardUpdate(UpdateView):
    model = Card
    fields = ['age', 'team', 'position', 'season']

class CardDelete(DeleteView):
    model = Card
    success_url = '/cards/'

def add_offer(request, card_id):
    form = OfferForm(request.POST)
    if form.is_valid():
        new_offer = form.save(commit=False)
        new_offer.card_id = card_id
        new_offer.save()
    return redirect('detail', card_id=card_id)