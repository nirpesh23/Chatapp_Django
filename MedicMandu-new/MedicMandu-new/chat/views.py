from django.shortcuts import render
from django.contrib.auth import get_user_model

User = get_user_model()

def chat_view(request):
    users = User.objects.exclude(username=request.user.username)
    return render(request, 'chat/chat_index.html', context={'users':users})


def main_chat(request, username):
    user_obj = User.objects.get(username=username)
    users = User.objects.exclude(username=request.user.username)
    return render(request, 'chat/main_chat.html', context={'users':users, 'user':user_obj})