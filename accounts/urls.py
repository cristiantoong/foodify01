from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as user_views

app_name = 'accounts'

urlpatterns = [
    path('login/', user_views.signin, name='login'),
    path('logout/', user_views.logout_view, name='logout'),
    path('register/', user_views.register, name='register'),
    path('create-profile/', user_views.create_profile, name='create_profile'),
    path('update-profile/', user_views.update_profile, name='update_profile'),
    path('profile/', user_views.view_profile, name='profile'),
    path('profile/<str:pk>/', user_views.view_profile_by_id, name='profile_by_id'),
]
