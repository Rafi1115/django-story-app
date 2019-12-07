from django import forms
from .models import Post
from django.contrib.auth import (authenticate)


class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    name = forms.CharField(max_length=100)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = (
            'title', 'overview', 'thumbnail', 'category'
        )
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
    
        super(PostForm, self).__init__(*args, **kwargs)
