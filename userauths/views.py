from django.shortcuts import render
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import redirect
from django.conf import settings

User= settings.AUTH_USER_MODEL


def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        print("Successful Registration! WooHoo!!")
        if form.is_valid():
            new_user =form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hey {username}, Account was successfuly created!")
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1']
                                    )
            login(request, new_user)
            return redirect ("core:index")
        
    else:
        print("You can't be registered :(")
        form = UserRegisterForm()
   
    context ={
        'form': form,
    }
    return render(request, "userauths/sign-up.html", context)

def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, f"Hey nani, you are already logged in ama?")
        return redirect("core:index")
    
    if request.method =="POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        try:
            user = User.objects.get(email=email)
        except:
            messages.warning(request, f"User with {email} does not exist")
            
        user= authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request,user)
            messages.success(request, "You are logged in!")
            return redirect("core:index")
        else:
            messages.warning(request, f"User does not exist, create an account")
            
    context ={
        
    }
            
    return render(request, "userauths/sign-in.html", context)