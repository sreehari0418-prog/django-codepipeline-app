from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome Sreehari - Version 1")
