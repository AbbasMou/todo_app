from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # saving the user
            username = form.cleaned_data.get('username')  # get the username
            messages.success(request,
                             f'account created for {username}')  # send a message that the account successfully created ,
            # message will be recieved by base.html where we are looping over messages if we have messages
            return redirect('login')  # after successful sign up, the user will be redirected to login page
        else:
            messages.error(request, 'Failed to create account ')
            form = UserRegisterForm
            return render(request, 'users/register.html', {'form': form})
    # it needs adding login_url to settings.py
    # after login sucedded , djando will search to url to go to it , we should add that to settings.py

    else:  # if the method is get,render the sign up page to let user enter his info
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})
