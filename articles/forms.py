from django import forms
from .models import  Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
