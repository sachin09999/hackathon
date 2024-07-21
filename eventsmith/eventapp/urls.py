from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import event_list
urlpatterns = [
    path('', views.home, name='home'),
    path('saveenquiry/',views.saveEnquiry,name='saveenquiry'),
    path('events/', event_list, name='event_list'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)