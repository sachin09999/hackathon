from django.shortcuts import render
from eventapp.models import contactEnquiry
from .models import Event

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
    
def event_list(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'event_list.html', context)



