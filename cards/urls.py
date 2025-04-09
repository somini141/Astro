from django.urls import path
from cards.views import show_info_cards

app_name = 'cards'

urlpatterns = [
    path('', show_info_cards, name='home'),
]
