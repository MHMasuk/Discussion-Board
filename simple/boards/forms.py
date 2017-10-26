from django import forms
from .models import Topic, Post


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'Whats in your mind?'}
        ),
        max_length=4000,
        help_text='The message should be between 4000 characters.')

    class Meta:
        model = Topic
        fields = ['subject', 'message']

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['message']
