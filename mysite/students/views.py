from django.shortcuts import render, redirect



def signup(request):
    return redirect("https://sso.university.innopolis.ru/adfs/oauth2/authorize/?client_id=b04c488e-95c4-47d1-824e-6806731565e5&response_type=code&redirect_uri=https://studprojectfeedback.innopolis.university/login/oauth/")

