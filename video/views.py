from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import CommentForm

def videos(request):
    videos_list = Video.objects.all()
    context = {"videos_list": videos_list}
    return render(request, 'videos.html', context)

def video(request, id):
    # 7
    # SELECT * FROM video_video WHERE id = 7;
    video_object = Video.objects.get(id=id)
    
    if request.user.is_authenticated:
        video_view, created = VideoView.objects.get_or_create(
            user=request.user,
            video=video_object,
         )
    context = {}     

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False) # ещё нет записи в БД
            comment.user = request.user
            comment.video = video_object
            comment.save() # сохраняем в БД
            messages.success(request, 'Комментарий успешно добавлен.')
            return redirect(video, id=video_object.id)
        else:
            messages.error(request, 'Ошибка! Данные не валидны')

    context = {
        "video": video_object,
        "comment_form": CommentForm()

    }


    return render(request, 'video.html', context)
        
def video_add(request):
    if request.method == "GET":
        return render(request, 'video_add.html')
    elif request.method == "POST":
        name = request.POST["video_name"]
        video_file = request.FILES["video_file"]
        video_object = Video(
            name=name,
            file_path=video_file,
        )
        # video_object.description = "hello world"
        # INSERT INTO ...
        video_object.save()
        return redirect(video, id=video_object.id)

def video_update(request, id):
    video_object = Video.objects.get(id=id)
    context = {"video": video_object}

    if request.method == "POST":
        name = request.POST["video_name"]
        video_object.name = name
        video_object.save()
        return redirect(video, id=video_object.id)

    return render(request, 'video_update.html', context)

def video_delete(request, id):
    video_object = Video.objects.get(id=id)
    video_object.delete()
    return redirect(videos)

def video_df_add(request):
    context = {}
    if request.method == "POST":
        # код создания playlist 

        # создаём объект формы с значениями
        video_form = VideoForm(request.POST)
        # проверка валидности
        if video_form.is_valid():
            # создаём запись в БД
            video_object = video_form.save()
            return redirect(video_info, id=video_object.id)
    
    video_form = VideoForm()
    context["video_form"] = video_form
    return render(request, "video_df_add.html", context) 
    


    