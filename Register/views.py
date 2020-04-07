from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from Register.models import ExtraInfo
from django.contrib import messages
import re


def register(request):
    if request.method == "POST":
        firstname = request.POST.get("fname")
        username = request.POST.get("username")
        age = request.POST.get("age")
        location = request.POST.get("location")
        lastname = request.POST.get("lname")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 == password2:
            password = password1
            check = 2
            while password:
                if (len(password) < 8 or len(password) > 12):
                    print('password less than 8 or greater than 12 ')
                    messages.error(request, 'password less than 8 or greater than 12 ')
                    return redirect('register')
                    check = 0
                    break
                elif not re.search("[a-z]", password):
                    print('password doesnt have a-z')
                    messages.error(request, 'password doesnt have characters between a-z')
                    return redirect('register')
                    check = 0
                    break
                elif not re.search("[0-9]", password):
                    print('password doesnt have numbers')
                    messages.error(request, 'password doesnt have numbers')
                    return redirect('register')
                    check = 0
                    break
                elif not re.search("[A-Z]", password):
                    print('password doesnt have A-Z')
                    messages.error(request, 'password doesnt have characters between A -Z')
                    return redirect('register')
                    check = 0
                    break
                elif not re.search("[$#@!%&^]", password):
                    print('password doesnt have special character')
                    messages.error(request, 'password doesnt have characters between A -Z')
                    return redirect('register')
                    check = 0
                    break
                elif re.search("\s", password):
                    print('password has space')
                    check = 0
                    break
                else:
                    print("Valid Password")
                    if User.objects.filter(username=username):
                        messages.error(request, 'Oops!! The username is taken. Try another.')
                        return redirect('register')
                    else:
                        if User.objects.filter(email=email):
                            messages.error(request, 'Oops!! The email is taken. Try another.')
                            return redirect('register')
                        else:
                            user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname,
                                                            email=email,
                                                            password=password1)

                            extraInfo = ExtraInfo(age=age, location=location, user=user)
                            extraInfo.save()
                            user.save()
                            check = 1
                            messages.success(request, 'User created')

                            return redirect('register')
            if check ==1:
                print('password standard matched')
            else:
                print('password standard did not match')
        else:
            messages.error(request, 'Your Passwords are different')
            return redirect('register')

    return render(request, 'Registration.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                print(user.username,' is logged in  ======================================================')
                return render(request, 'user.html')
            else:
                print('user is disabled')
                return redirect('signin')
        else:
            print('*******************************************username or password is wrong')
    else:
        return render(request, 'home.html')

def logout_user(request):
    messages.success(request, 'You have logged out successfully.')
    logout(request)
    return redirect('signin')