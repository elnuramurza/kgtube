from django.shortcuts import render, HttpResponse
from .models import Video

# Create your views here.
def homepage(request):
    # return HttpResponse("hello world")
    return render(request, "home.html")

def about_view(request):
    return render(request, 'about.html')

# def video_list(request):
#     videos = Video.objects.all()
#     return render(request, 'video_list.html', {'videos': videos})
   

   
   