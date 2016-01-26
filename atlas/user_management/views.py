from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect

from .forms import UserForm

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
                message = "Your account is disabled, please contact your system admin."
                return render(request, 'user_management/login.html', {'message':message})
        else:
            message = "Invalid Login Credentials, please try again."
            return render(request, 'user_management/login.html', {'message':message})
    else:
        if request.user.is_authenticated():
            return HttpResponseRedirect('/jsslabelwriter')
        else:
            return render(request, 'user_management/login.html', {})

@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/user_management/login/')

@login_required
def index(request):
    user_list = User.objects.all().order_by("last_name", "first_name")
    return render(request, 'user_management/index.html', { 'user_list':user_list })

@login_required
def detail(request, user_id):
    person = get_object_or_404(User, pk=user_id)
    return render(request, 'user_management/detail.html', {'person':person})

@login_required
def edit(request, user_id):
    person = get_object_or_404(User, pk=user_id)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return render(request, 'user_management/detail.html', {'person':person} )
        else:
            return render(request, 'user_management/edit.html', {'form':form, 'person':person})
    else:
        form = UserForm(instance=person)
        return render(request, 'user_management/edit.html', {'form':form, 'person':person })

@login_required
def create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            person = form.save()
            return render(request, 'user_management/detail.html', {'person':person})
        else:
            return render(request, 'user_management/create.html', {'form':form})
    else:
        form = UserForm()
        return render(request, 'user_management/create.html', {'form':form})

@login_required
def delete(request, user_id):
    person = get_object_or_404(User, pk=user_id)
    person.delete()

    return redirect('/user_management/')

@login_required
def change_status(request, user_id):
    person = get_object_or_404(User, pk=user_id)
    if person.is_active:
        person.is_active = False
    else:
        person.is_active = True
    person.save()

    return redirect('/user_management/' + str(person.id))
