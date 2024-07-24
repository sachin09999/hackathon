from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import event_list,event_comments
from .admin_views import admin_chat_room
from .views import admin_chat
from .views import payment_view,process_payment_view
urlpatterns = [
    path('', views.home, name='home'),
    path('saveenquiry/',views.saveEnquiry,name='saveenquiry'),
    path('events/', event_list, name='event_list'),
    path('admin-chat/<str:room_name>/', admin_chat_room, name='admin_chat_room'),
    path('chat/<str:room_name>/', views.chat_room, name='chat_room'),
    path('send_message/', views.send_message, name='send_message'),
    path('admin_chat/', admin_chat, name='admin_chat'),
    path('create/', views.create_event, name='create_event'),
    path('payment/<int:event_id>/', payment_view, name='payment'),
    path('process_payment/<int:event_id>/', process_payment_view, name='process_payment'),
    path('comments/<int:event_id>/', event_comments, name='event_comments'),
]
    
    
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)