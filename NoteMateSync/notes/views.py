from django.shortcuts import render,redirect
from .models import Like,Post
# Create your views here.

def note_view(request):
    qs=Post.objects.all()
    user=request.user

    context={
        'qs':qs,
        'user':user,
    }

    return render(request,'notes.html',context)

# def like_note(request):
#     return redirect('notes:note-list')