from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from parqueadero.forms.userForm import admin
from django.shortcuts import render, redirect


def loginView(request):
    if request.method == 'POST':
        _username= request.POST['username']
        _password= request.POST['password']
        user= authenticate(request, username=_username, password=_password)
        print(user)

        if user:
            login(request,user)
            return redirect('principal')
        else:
            return  render(request,'webPage/login.html', {'error':' El usuario no se encuentra registrado'})

    return render(request,'webPage/login.html')

@permission_required("parqueadero.add_user")
def register(request):
    data = {
        'form' : admin()
    }
    if request.method == 'POST':
        formulario = admin(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],
                                password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect("principal")
            data
    return render(request, 'webPage/registerUser.html', data)


@login_required
def logoutView(request):
    logout(request)
    return render(request, 'webPage/login.html')