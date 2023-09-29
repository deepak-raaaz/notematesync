from django.urls import path
from .views import note_view,like_note

app_name = 'notesapp'

urlpatterns = [
    path('',note_view,name='note-list'),
    path('like/',like_note,name='like-note')
    
]
