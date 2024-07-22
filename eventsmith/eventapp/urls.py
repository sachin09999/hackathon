from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import event_list
from .admin_views import admin_chat_room
from .views import admin_chat
urlpatterns = [
    path('', views.home, name='home'),
    path('saveenquiry/',views.saveEnquiry,name='saveenquiry'),
    path('events/', event_list, name='event_list'),
    path('admin-chat/<str:room_name>/', admin_chat_room, name='admin_chat_room'),
    path('chat/<str:room_name>/', views.chat_room, name='chat_room'),
    path('send_message/', views.send_message, name='send_message'),
    path('admin_chat/', admin_chat, name='admin_chat'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)