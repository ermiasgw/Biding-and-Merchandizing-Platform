from django.urls import path, re_path
from . import views
from django.views.generic import TemplateView
from dj_rest_auth.registration.views import VerifyEmailView,ResendEmailVerificationView
from dj_rest_auth.views import LogoutView, PasswordResetView, PasswordResetConfirmView, PasswordChangeView

urlpatterns = [
    path('user-register/', views.userSignUpView.as_view(), name="user_register" ),
    path('organization-register/', views.orgSignUpView.as_view(), name="organization_register"),
    path('account-confirm-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
    path('resend-email/', ResendEmailVerificationView.as_view(), name="rest_resend_email"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('password/reset/', PasswordResetView.as_view(), name="password_reset"),
    path('password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password_change/', PasswordChangeView.as_view(), name="password_chage"),
    re_path(
        r'^account-confirm-email/(?P<key>[-:\w]+)/$', views.email_confirm_redirect,
        name='account_confirm_email',
    ),
    path(
        'account-email-verification-sent/', TemplateView.as_view(),
        name='account_email_verification_sent',
    ),

]