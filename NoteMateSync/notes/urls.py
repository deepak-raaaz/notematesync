from django.urls import path
from notes import views
app_name='notes'
urlpatterns = [
   path('notes',views.note_view,name='note-list'),
   path('like/',views.like_note,name='like-list'),
   
]
