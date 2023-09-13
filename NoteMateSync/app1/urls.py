from django.urls import path
from app1 import views

urlpatterns = [
   path('',views.home,name='home'),
   
   path('notes-view/',views.notesview,name='notesview'),
   path('college/',views.college,name='college'),
   path('club/',views.club,name='club'),
]
