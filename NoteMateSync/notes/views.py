from django.shortcuts import render
from .models import Like,Note
# Create your views here.

def note_view(request):
    qs=Note.objects.all()
    user=request.user

    context={
        'qs':qs,
        'user':user,
    }

    return render(request,'notes.html',context)

