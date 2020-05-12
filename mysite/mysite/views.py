from django.views import View
from django.shortcuts import redirect

class AuthView(View):
    def get(self, request, *args, **kwargs):
        print(f"{request.GET}\n{args}\n{kwargs}")
        return redirect("/")
