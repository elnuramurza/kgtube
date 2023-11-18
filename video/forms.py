from django import forms
from .models import UserVideo


class VideoForm(forms.ModelForm):
    class Meta:
        model = UserVideo
        fields = ['name', 'description', 'videos_qty']