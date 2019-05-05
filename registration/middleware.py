from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.middleware.http import MiddlewareMixin


class AuthRequiredMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse('registration/login.html'))
        return None
