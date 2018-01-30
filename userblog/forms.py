from django import forms

from .models import UserPost

class PostForm(forms.ModelForm):
#class Meta, where we tell Django which model should be used to create this form (model = UserPost).
    class Meta:
        model = UserPost
        fields = ('title', 'text',)
