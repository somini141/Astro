from django.shortcuts import render
from .models import CardTaro


def show_info_cards(request):
    cards = CardTaro.objects.all()
    # Преобразуем QuerySet в список словарей для удобной работы в JS
    cards_data = [{
        'name': card.name,
        'description_meaning': card.description_meaning,
        'description_advance': card.description_advance,
        'image': card.image.url if hasattr(card.image, 'url') else card.image  # Обработка как FileField или CharField
    } for card in cards]

    return render(request, 'main.html', {
        'cards_json': cards_data  # Передаем данные в JSON формате
    })
