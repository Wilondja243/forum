from django.urls import re_path

from .consumers import ChatConsummer

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", ChatConsummer.as_asgi()),
]