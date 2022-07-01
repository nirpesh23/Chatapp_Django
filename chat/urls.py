from django.urls import URLPattern, path
from chat.views import chat_view, main_chat

urlpatterns = [
    path('', chat_view, name='chat'),
    path('<str:username>', main_chat, name='main_chat')
]