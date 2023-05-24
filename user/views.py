from django.shortcuts import render
from  dj_rest_auth.registration.views import RegisterView
from .serializers import IndividualRegistrationSerializer, OrganizationRegistrationSerializer

# Create your views here.
class userSignUpView(RegisterView):
    serializer_class = IndividualRegistrationSerializer

class orgSignUpView(RegisterView):
    serializer_class = OrganizationRegistrationSerializer
    