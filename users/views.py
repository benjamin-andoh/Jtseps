from django.contrib import messages
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
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


def profile(request):
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user)
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST)
        p_form = ProfileUpdateForm(request.POST)
        if p_form.is_valid() and u_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'account has been create for update successfully')
            return redirect('users:profile')
    context = {
        'u_form': u_form, 'p_form': p_form
    }
    return render(request, 'profile.html', context)
