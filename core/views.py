from django.shortcuts import render, HttpResponse
from video.models import Video
from django.shortcuts import render, redirect
from .forms import ProfileForm


# Create your views here.
def homepage(request):
    # return HttpResponse("hello world")
    return render(request, "home.html")

def about_view(request):
    return render(request, 'about.html')

def search(request):
    key_word = request.GET["key_word"]
    # SELECT * FROM Video WHERE name LIKE '%key_word%'
    videos_query = Video.objects.filter(name__contains=key_word)
    context = {"videos_list": videos_query}
    return render(request, "videos.html", context)

   
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
    if form.is_valid():
        profile = form.save(commit=False)
        profile.user = request.user
        profile.save()
        return redirect('home')  # Redirect to your home page
    else:
        form = ProfileForm()

    return render(request, 'profile.html', {'form': form})
   
