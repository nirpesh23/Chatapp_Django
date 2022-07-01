"""
ASGI config for MedicMandu project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from chat.consumers import PersonalChatConsumer


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MedicMandu.settings')

application = get_asgi_application()

application = ProtocolTypeRouter({
    # "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path('ws/<int:id>/', PersonalChatConsumer.as_asgi())
        ])
    )
})
