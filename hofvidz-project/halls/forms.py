# This form enables the user to import a video

from .models import Video
from django import forms

# This automatically creates a form for the model passed into it. From .models
# we import Video, so this is the model passed into this.

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['url']
        labels = {'url':'YouTube URL'}

class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=255, label='Search for videos:')
