from django.shortcuts import render
from app.models import *

# Create your views here.
def display_topics(request):
    lot=Topic.objects.all()
    d={'topics':lot}
    return render(request,'display_topics.html',context=d)

def display_webp(request):
    wp=Webpage.objects.all()
    d={'web':wp}
    return render(request,'display_webp.html',context=d)
