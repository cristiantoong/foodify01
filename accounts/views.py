from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UserChangeForm,
    PasswordChangeForm
)
from .forms import UserRegistrationForm, UserProfileForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy



def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('recipes:recipes_view')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }

    return render(request, 'accounts/signin.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! Your are now able to log in')
            return redirect('accounts:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form':form})

def logout_view(request):
        logout(request)
        return redirect('recipes:home')

@login_required
def create_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.profile_name = request.user
            obj.is_active = True
            obj.save()
            
            messages.success(request, f'Your Profile has been created!')
            return redirect('accounts:profile')
    else:
        form = UserProfileForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/create_profile.html', {'form':form})


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)

        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
    else:
        form = UserProfileForm(instance=request.user.userprofile)

   

    context = {'form': form}
    return render(request, 'accounts/update_profile.html', context)


@login_required
def view_profile(request):
    user_profile = UserProfile.objects.filter(profile_name=request.user)
    
    context = {
        'user_profile': user_profile,
        }
    return render(request, 'accounts/profile.html', context)


@login_required
def view_profile_by_id(request, pk):
    user_profile = UserProfile.objects.all()
    user_profile_by_id = get_object_or_404(UserProfile, pk=pk)
    
    context = {
        'user_profile': user_profile,
        'user_profile_by_id': user_profile_by_id,
        }
    return render(request, 'accounts/profile_by_id.html', context)







