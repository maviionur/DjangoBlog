from django import forms
from . import models


class CreateArticle(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}))
    title.label = ""
    slug = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Slug'}))
    slug.label = ""
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Article'}))
    body.label = ""

    class Meta:
        model = models.Article
        fields = ['title', 'body', 'slug', 'thumb']
