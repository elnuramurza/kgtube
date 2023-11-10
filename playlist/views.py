from django.shortcuts import render
from .models import UserPlayList
from .models import Video

# Create your views here.
def playlists(request):
    # SELECT * FROM UserPlayList;
    query_result = UserPlayList.objects.all()

    # query_result является списком 
    context = {"objects_list": query_result}

   def video_list(request):
       videos = Video.objects.all()
       
    return render(
        request, 
        'video_list.html', {'videos': videos})
   
    
    return render(
        request,
        'playlists.html',
        context
    )
