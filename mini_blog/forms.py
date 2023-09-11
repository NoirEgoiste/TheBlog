from django import forms
from .models import Post, Comment, Category

"""Your custom post categories"""

choices = [('coding', 'coding'), ('sport', 'sport'),
           ('Information Security', 'Information Security'),
           ('biotechnology', 'biotechnology'),
           ('AI', 'AI'), ('other', 'other')]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag',
                  'category', 'body', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter Title'
            }),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(
                choices=choices,
                attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter Title'
            }),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body',)

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter Name'}),
            'body': forms.Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Enter Comment'
            }),
        }
