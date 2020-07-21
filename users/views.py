from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from users.forms import UserRegistrationForm
from .forms import UserUpdateForm, ProfileUpdateForm


def register_page(request):
    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' + username)
            return redirect('users:login')

    context = {'form': form}
    return render(request, 'register.html', context)


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        login(request, user)
        if user is not None:
            login(request, user)
            return redirect('home:home')
        else:
            messages.info(request, "username or password incorrect")
    return render(request, 'login.html', {})


def logout_page(request):
    logout(request)
    return redirect("users:login")


def profile(request):
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user)
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid() and u_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'account updated successfully')
            return redirect('users:profile')
    context = {
        'u_form': u_form, 'p_form': p_form
    }
    return render(request, 'profile.html', context)


def list_employee(request):
    users = User.objects.all()
    return render(request, 'employee/employee_list.html', {'users': users})
