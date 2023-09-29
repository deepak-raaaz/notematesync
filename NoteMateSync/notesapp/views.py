from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def note_view(request):
    qs=Note.objects.all()
    user = request.user

    context={
        'qs':qs,
        'user':user,
    }

    return render(request,'notes.html',context)

def like_note(request):
    user = request.user
    if request.method=='POST':
        note_id=request.POST.get('note_id')
        note_obj=Note.objects.get(id=note_id)

        if user in note_obj.liked.all():
            note_obj.liked.remove(user)
        else:
            note_obj.liked.add(user)
        
        like,created=Like.objects.get_or_create(user=user,note_id=note_id)

        if not created:
            if like.value=='Like':
                like.value=='Unlike'
            else:
                like.value='Like'

        like.save()            

            
    return redirect('notesapp:note-list')
