from django.contrib import admin
from django.urls import path

from notes import views
app_name='notes'
urlpatterns = [
    path('',views.note_view,name='note-list')
    
]