from django.contrib.auth.forms import UserCreationForm, UserChangeForm, \
    PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from mini_blog.models import Profile


class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic', 'website_url', 'telegram',
                  'facebook_url', 'twitter_url', 'instagram_url', 'vkontakte']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
            'website_url': forms.URLInput(attrs={'class': 'form-control'}),
            'telegram': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
            'vkontakte': forms.TextInput(attrs={'class': 'form-control'}),
        }


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Email'}
        )
    )
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    first_name = forms.CharField(max_length=100,
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control'})
                                 )
    last_name = forms.CharField(max_length=100,
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control'})
                                )
    username = forms.CharField(max_length=100,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control'})
                               )
    last_login = forms.CharField(max_length=100,
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control'})
                                 )
    date_joined = forms.CharField(max_length=100,
                                  widget=forms.TextInput(
                                      attrs={'class': 'form-control'}))
    is_superuser = forms.CheckboxInput(attrs={'class': 'form-check'})
    is_stuff = forms.CheckboxInput(attrs={'class': 'form-check'})
    is_active = forms.CheckboxInput(attrs={'class': 'form-check'})

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'email',
            'password', 'is_active', 'last_login', 'date_joined',
        )


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.PasswordInput(attrs={'class': 'form-control',
                                              'type': 'password'})
    new_password1 = forms.PasswordInput(attrs={'class': 'form-control',
                                               'type': 'password'})
    new_password2 = forms.PasswordInput(attrs={'class': 'form-control',
                                               'type': 'password'})

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
