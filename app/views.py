from django.shortcuts import render
from app.models import *
from django.

# Create your views here.
def display_topics(request):
    lot=Topic.objects.all()
    d={'topics':lot}
    return render(request,'display_topics.html',context=d)

def display_webp(request):
    wp=Webpage.objects.all()
    wp=Webpage.objects.order_by('name')
    wp=Webpage.objects.order_by('-name')
    wp=Webpage.objects.all()[:2:]
    wp=Webpage.objects.filter(topic_name='cricket')
    wp=Webpage.objects.order_by('-name')
    d={'web':wp}
    return render(request,'display_webp.html',context=d)

def display_access(request):
    ar=Accessrecord.objects.all()
    d={'accessr':ar}
    return render(request,'display_access.html',context=d)
