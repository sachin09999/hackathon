from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def admin_chat_room(request, room_name):
    return render(request, 'admin_chat.html', {'room_name': room_name})
