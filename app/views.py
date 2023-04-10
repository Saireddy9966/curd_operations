from django.shortcuts import render
from app.models import *
from django.db.models.functions import *
from django.db.models import Q


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
    #wp=Webpage.objects.filter(name_startswith='D')
    #wp=Webpage.objects.filter(url_endswith='D')
    #wp=Webpage.objects.filter(Q(topic_name='Cricket') & Q(name='dhoni'))
    wp=Webpage.objects.all()
    d={'web':wp}
    return render(request,'display_webp.html',context=d)

def display_access(request):
    ar=Accessrecord.objects.all()
    ar=Accessrecord.objects.filter(date__gt='2002-11-25')
    ar=Accessrecord.objects.filter(date__gte='2019-5-16')
    ar=Accessrecord.objects.filter(date__year__gte='2019')
    ar=Accessrecord.objects.all()
    ar=Accessrecord.objects.filter(date__month='4')
    ar=Accessrecord.objects.filter(date__day='12')
    ar=Accessrecord.objects.all()
    
    
    
    d={'accessr':ar}
    return render(request,'display_access.html',context=d)
