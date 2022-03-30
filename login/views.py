from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_site(request):

    if request.method == "POST":
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
        else:
            print(f"Something get wrong!")

    if request.user.is_authenticated:
        return redirect('/')

    return render(request, 'login.html', {})


def logout_site(request):
    logout(request)
    return redirect('login')