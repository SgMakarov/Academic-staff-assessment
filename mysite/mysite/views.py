from django.views import View
from django.shortcuts import redirect
import requests


class AuthView(View):
    def get(self, request, *args, **kwargs):
        print(request.GET.get('code'))
        token = {
            "grant_type": "authorization_code",
            "code": request.GET.get('code'),
            "response_type": "code",

            "client_id": "b04c488e-95c4-47d1-824e-6806731565e5",
            "client_secret": "JPAHZDIhjh-o1e6XqDBEsnkjx2H_eJI_guJ1iZth",

            "redirect_uri": "https://studprojectfeedback.innopolis.university"
        }
        resp = requests.post("https://sso.university.innopolis.ru/adfs/oauth2/token", data=token, headers={
            'content-type': 'application/json'
        })
        print(token)
        data = resp.json()
        print(data)
        return redirect("/")
