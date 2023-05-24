from django.urls import path
from . import views

urlpatterns = [
    path('user-register', views.userSignUpView.as_view(), name="user_register" ),
    path('organization-register', views.orgSignUpView.as_view(), name="organization_register"),

]