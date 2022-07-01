from email import message
from django.shortcuts import render
from django.contrib.auth import get_user_model
from chat.models import ChatModel

User = get_user_model()

def chat_view(request):
    users = User.objects.exclude(username=request.user.username)
    return render(request, 'chat/chat_index.html', context={'users':users})


def main_chat(request, username):
    user_obj = User.objects.get(username=username)
    users = User.objects.exclude(username=request.user.username)

    if request.user.id > user_obj.id:
        thread_name = f'chat_{request.user.id}-{user_obj.id}'
    else:
        thread_name = f'chat_{user_obj.id}-{request.user.id}'
    message_obj = ChatModel.objects.filter(thread_name=thread_name)
    return render(request, 'chat/main_chat.html', context={'users':users, 'user':user_obj, 'messages':message_obj})