from django.shortcuts import render, redirect
from django.contrib import messages
import requests
import logging
from .forms import SiteUserForm

logger = logging.getLogger(__name__)

TELEGRAM_TOKEN = ''
TELEGRAM_CHAT_ID = ''


def home(request):
    form = SiteUserForm()
    return render(request, 'main.html', {'form': form})


def send_telegram_message(text):
    try:
        response = requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
            json={
                'chat_id': TELEGRAM_CHAT_ID,
                'text': text,
                'parse_mode': 'HTML'
            },
            timeout=5
        )
        return response.status_code == 200
    except Exception as e:
        logger.error(f"Telegram error: {str(e)}")
        return False


def connecting(request):
    if request.method == 'POST':
        form = SiteUserForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()

                message = (
                    "<b>Новая заявка!</b>\n"
                    f"<b>ФИО:</b> <code>{user.full_name}</code>\n"
                    f"<b>Email:</b> <code>{user.email}</code>\n"
                    f"<b>Телефон:</b> <code>{user.phone}</code>\n"
                )

                if send_telegram_message(message):
                    messages.success(request, 'Форма успешно отправлена!')
                else:
                    messages.warning(request, 'Заявка сохранена, но не отправлена в Telegram')

                response = redirect('user:home')
                response['Location'] += '#feedback-form'
                return response

            except Exception as e:
                messages.error(request, f'Ошибка при сохранении: {str(e)}')
                response = redirect('user:home')
                response['Location'] += '#feedback-form'
                return response
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме')
            response = redirect('user:home')
            response['Location'] += '#feedback-form'
            return response
    else:
        form = SiteUserForm()

    return redirect('user:home')
