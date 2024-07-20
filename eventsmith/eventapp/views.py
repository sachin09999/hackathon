from django.shortcuts import render,get_object_or_404, redirect
from .models import Event
from .forms import RSVPForm

# Create your views here.

def home(request):
    return render(request,"home.html")

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = RSVPForm(request.POST)
        if form.is_valid():
            rsvp = form.save(commit=False)
            rsvp.event = event
            rsvp.save()
            return redirect('event_detail', event_id=event.id)
    else:
        form = RSVPForm()
    return render(request, 'event_detail.html', {'event': event, 'form': form})
