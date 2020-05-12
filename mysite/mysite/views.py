from django.views import View

class AuthView(View):
    def get(self, request):
        data = request.data
        print(data.get("code"))