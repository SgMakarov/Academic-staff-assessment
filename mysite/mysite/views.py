from django.views import View

class AuthView(View):
    def post(self, request):
        print(request.data)