from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import UserRegisterForm


# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()  # saving the user
#             username = form.cleaned_data.get('username')  # get the username
#             messages.success(request,
#                              f'account created for {username}')  # send a message that the account successfully created ,
#             # message will be recieved by base.html where we are looping over messages if we have messages
#             return redirect('login')  # after successful sign up, the user will be redirected to login page
#         else:
#             messages.error(request, 'Failed to create account ')
#             form = UserRegisterForm
#             return render(request, 'users/register.html', {'form': form})
#     # it needs adding login_url to settings.py
#     # after login sucedded , djando will search to url to go to it , we should add that to settings.py
#
#     else:  # if the method is get,render the sign up page to let user enter his info
#         form = UserRegisterForm()
#         return render(request, 'users/register.html', {'form': form})


#method that deals with unique email and username
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account created for {username}. You can now log in.')
                return redirect('login')
            else:
                # Display a failure message if the form is not valid
                messages.error(request, 'Failed to create an account. Please fix the errors below.')
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})
