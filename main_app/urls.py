from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cards/', views.cards_index, name='index'),
    path('cards/<int:card_id>/', views.cards_detail, name='detail'),
    path('cards/create/', views.CardCreate.as_view(), name='cards_create'),
    path('cards/<int:pk>/update/', views.CardUpdate.as_view(), name='cards_update'),
    path('cards/<int:pk>/delete/', views.CardDelete.as_view(), name='cards_delete'),
    path('cards/<int:card_id>/add_offer/', views.add_offer, name='add_offer'),
    path('cases/', views.CaseList.as_view(), name='cases_index'),
    path('cases/create/', views.CaseCreate.as_view(), name='cases_create'),
    path('cases/<int:pk>', views.CaseDetail.as_view(), name='cases_detail'),
    path('cases/<int:pk>/update/', views.CaseUpdate.as_view(), name='cases_update'),
    path('cases/<int:pk>/delete/', views.CaseDelete.as_view(), name='cases_delete'),
    path('cases/<int:card_id>/add_assoc/<int:case_id>/', views.add_assoc, name='add_assoc'),
    path('cases/<int:card_id>/remove_assoc/<int:case_id>/', views.remove_assoc, name='remove_assoc'),
    path('accounts/signup/', views.signup, name='signup'),
]