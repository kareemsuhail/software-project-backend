from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.shortcuts import HttpResponse
import jwt
@csrf_exempt
@require_http_methods([ "POST"])
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = User.objects.get(username=username)
    if user is not None:
        if user.check_password(password):
            user_data = {'username':user.username}
            token = jwt.encode(user_data,settings.SECRET_KEY)

            return JsonResponse({"token":token.decode('utf-8'),"msg":"success"})

    return JsonResponse(settings.NOT_AUTHENTICATED_MSG)
def register(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    try:
        User.objects.create(username=username,password=password,email=email)
    except Exception:
        return HttpResponse("sorry an error occurred")
def testLogin(request):
    print(request.user)
    return HttpResponse("yes")



