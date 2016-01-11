from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

def user_login(request):
    # If the request is POST the user is attempting to login.
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        # If user exists then the login credentials are correct
        if user:
            #Check if account is active
            if user.is_active:

                login(request, user)
                return HttpResponseRedirect('/jsslabelwriter')
            else:
                return HttpResponse('Your Atlas account has been disabled, please contact your system administrator')
        else:
            print "Invalid Login credentials: {0}, {1}".format(username,password)
            return HttpResponse("Invalid Login details were supplied")
    else:
        if request.user.is_authenticated():
            return HttpResponseRedirect('/jsslabelwriter')
        else:
            return render(request, 'user_management/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    
    return HttpResponseRedirect('/user_management/login')
