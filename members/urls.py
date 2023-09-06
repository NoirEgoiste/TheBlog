from django.urls import path

from .views import (UserRegisterView, UserEditView, PasswordsChangeView,
                    password_success, ShowProfilePageView,
                    EditProfilePageView, CreateProfilePageView)


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit-profile'),
    path('password/', PasswordsChangeView.as_view(), name='password-change'),
    path('password_success', password_success, name='password_success'),
    path('profile/<int:pk>',
         ShowProfilePageView.as_view(), name='show-profile-page'),

    path('edit_profile_page/<int:pk>',
         EditProfilePageView.as_view(), name='edit_profile_page'),

    path('create_profile_page/',
         CreateProfilePageView.as_view(), name='create_profile_page')
]
