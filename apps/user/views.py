from typing import Optional
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .models import User


# Create your views here.
def user_list(request):
    users = User.objects.all()
    #user_cnt = users.count()
    
    
    context = {'users': users}
    
    return render(request, "user/user_list.html", context)


def login_view(request):
    error_message = None
    
    # Unbound state of our form
    form = AuthenticationForm()
    
    if request.method == 'POST':
        #
        form = AuthenticationForm(data=request.POST) # kw argument
        
        # Validate the data
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            
            # Authenticate the user, if s, will return user object
            user: Optional[user] = authenticate(
                username=username,
                password=password,
            )
            # check if user was authenticated
            if user is not None:
                # use the session to keep the authenticated user's id
                login(request, user)
                # when we login, session will store user id
                # Authentication Middleware is going to use that id
                # and fetch 
                request.user
                # Redirect the user to his profile page
                # The url path name
                return redirect('profile')
            # TODO: If user is not authenticated, what should you do?
        
        else:
            # User's data is not valid. So, set an error msg to be displayed
            error_message = "Sorry, something went wrong. Try Again"
    
    context = {'form':form, "error_message": error_message}
    
    return render(request, "user/login.html", context)


def profile(request):
    return render(
        request,
        'user/profile.html'
    ) 