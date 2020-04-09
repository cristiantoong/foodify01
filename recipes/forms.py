from django.forms import ModelForm
from .models import Recipe, Comment
from django import forms



class RecipeForm(ModelForm):
    #content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 20}))

    class Meta:
        model = Recipe
        exclude = ('author', 'comment_count')
    

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'rows': 4
    }), label='')

    class Meta:
        model = Comment
        fields = ('content',)


