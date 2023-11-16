from django.shortcuts import render
from .models import UserPlayList

# Create your views here.
def playlist(request):
    # SELECT * FROM UserPlayList;
    query_result = UserPlayList.objects.all()

    # query_result является списком 
    context = {"objects_list": query_result}

    return render(
        request,
        'playlist.html',
        context
    )
def playlist_add(request):
    if request.method == "GET":
        return render(request, 'playlist_add.html')
    elif request.method == "POST":
        name = request.POST["playlist_name"]
        playlist_file = request.FILES["playlist_file"]
        playlist_object = playlist(name=name,
        file_path=playlist_file,
    
        )
        # video_object.description = "hello world"
        # INSERT INTO ...
        playlist_object.save()
        return redirect(playlist, id=playlist_object.id)
           