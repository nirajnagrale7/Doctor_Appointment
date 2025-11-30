from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required # Import login_required
from .forms import AdminRegisterForm, UserUpdateForm, UserProfileUpdateForm, AdminLoginForm # Import new forms
from .models import UserProfile # Import UserProfile
from django.contrib.auth.models import User

# Create your views here.
def admin_register(request):
    if request.method == 'POST':
        form = AdminRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create a UserProfile for the new user
            UserProfile.objects.create(user=user)
            messages.success(request, 'Your account has been created! You are now able to log in.')
            return redirect('login') # Redirect to login page
    else:
        form = AdminRegisterForm()
    return render(request, 'admin_panel/admin_register.html', {'form': form})

def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You have successfully logged in as {username}.")
                return redirect('dashboard') # Redirect to a dashboard page
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AdminLoginForm()
    return render(request, 'admin_panel/admin_login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'admin_panel/admin_dashboard.html')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UserProfileUpdateForm(request.POST, instance=request.user.userprofile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UserProfileUpdateForm(instance=request.user.userprofile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'admin_panel/profile.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'admin_panel/change_password.html', {'form': form})

def custom_logout_view(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('login')