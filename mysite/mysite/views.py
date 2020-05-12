from django.views import View
from django.shortcuts import redirect

class AuthView(View):
    def get(self, request):
        data = request.data
        print(data.get("code"))
        return redirect("/")
    def post(self, request):
        data = request.data
        print(data.get("code"))
        return redirect("/")
