from django.shortcuts import render
from  dj_rest_auth.registration.views import RegisterView
from .serializers import IndividualRegistrationSerializer, OrganizationRegistrationSerializer,CustomLoginSerializer
from django.http import HttpResponseRedirect
from dj_rest_auth.views import LoginView

# Create your views here.
class userSignUpView(RegisterView):
    serializer_class = IndividualRegistrationSerializer

class orgSignUpView(RegisterView):
    serializer_class = OrganizationRegistrationSerializer
    
def email_confirm_redirect(request, key):
    return HttpResponseRedirect(
        f"{settings.EMAIL_CONFIRM_REDIRECT_BASE_URL}{key}/"
    )

class LoginView(LoginView):
    serializer_class = CustomLoginSerializer