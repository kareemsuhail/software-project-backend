from django.shortcuts import HttpResponse
from django.utils.six import text_type
from django.contrib.auth.models import User
from django.conf import settings
import jwt
class JWTAuthMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self, request):
        print("request path  is: " + request.path)
        if "rest" in request.path:
            print("this request needs authorization")
            auth = request.META.get('HTTP_AUTHORIZATION', b'')
            print(auth)
            if isinstance(auth, text_type):
                try:
                    decoded = jwt.decode(request.META['HTTP_AUTHORIZATION'],settings.SECRET_KEY)
                    print("username is {}".format(decoded['username']))
                    request.user = User.objects.get(username=decoded['username'])
                    response = self.get_response(request)
                    return response
                except Exception:
                    return HttpResponse("user data is not correct",status=401)
        response = self.get_response(request)
        return response
