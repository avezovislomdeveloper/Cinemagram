from django import forms
from . models import Comment, Rating


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        
        

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['score']  # Only include the fields you want users to submit

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['score'].widget = forms.Select(choices=[(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)])