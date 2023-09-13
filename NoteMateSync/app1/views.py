from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,'index.html')



def notesview(request):
    return render(request,'notes-view.html')

def college(request):
    return render(request,'college-view.html')

def club(request):
    return render(request,'club.html')