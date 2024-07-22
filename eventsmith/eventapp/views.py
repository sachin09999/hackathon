from django.shortcuts import render
from eventapp.models import contactEnquiry
from .models import Event
from django.http import JsonResponse
import pusher
import json
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import ChatMessage

# Create your views here.

def home(request):
    return render(request,"home.html")

def saveEnquiry(request):
    if request.method=='POST':
        name=request.POST.get('name')
        description=request.POST.get('description')
        date=request.POST.get('date')
        time=request.POST.get('time')
        photo=request.POST.get('photo')
        en=contactEnquiry(name=name,description=description,date=date,time=time,photo=photo)
        en.save()

    return render(request,"createvent.html")
    
# def event_list(request):
#     events = Event.objects.all()
#     if request.method=="GET":
#         et=request.GET.get('event')
#         if et!=None:
#             events = Event.objects.filter(name=events)

#     context = {'events': events}
#     return render(request, 'event_list.html', context)

def event_list(request):
    event = request.GET.get('event', None)
    if event:
        # Ensure 'event' is not being used in a way that expects a single result
        events = Event.objects.filter(name=event)  # 'name' should be the field you are filtering by
    else:
        events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def chat_room(request, room_name):
    return render(request, 'chat.html', {'room_name': room_name})
# Initialize Pusher
pusher_client = pusher.Pusher(
    app_id=settings.PUSHER_APP_ID,
    key=settings.PUSHER_KEY,
    secret=settings.PUSHER_SECRET,
    cluster=settings.PUSHER_CLUSTER,
    ssl=True
)
@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data.get('message')
        room = data.get('room')
        sender = data.get('sender')  # This should be 'client' or 'admin'

        # Save the message to the database
        ChatMessage.objects.create(
            room=room,
            sender=sender,
            message=message
        )

        # Trigger a Pusher event
        pusher_client.trigger(
            f'chat_{room}',
            'message',
            {'message': message, 'sender': sender}
        )

        return JsonResponse({'status': 'Message sent'})
    return JsonResponse({'status': 'Invalid request'}, status=400)

@csrf_exempt
def admin_reply(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data.get('message')
        room = data.get('room')

        # Save the reply to the database
        ChatMessage.objects.create(
            room=room,
            sender='admin',
            message=message
        )

        # Trigger a Pusher event
        pusher_client.trigger(
            f'chat_{room}',
            'message',
            {'message': message, 'sender': 'admin'}
        )

        return JsonResponse({'status': 'Message sent'})
    return JsonResponse({'status': 'Invalid request'}, status=400)

def admin_chat(request):
    room_name = 'room_name'  # Or any logic to get the room name dynamically
    return render(request, 'admin_chat.html', {'room_name': room_name})
