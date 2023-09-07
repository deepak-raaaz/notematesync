
from django.urls import path
from app import views

urlpatterns = [
   path('',views.home,name='home'),
   path('notes/',views.notes,name='notes'),
   path('notes-view/',views.notesview,name='notesview'),
   path('college/',views.college,name='college'),
]
