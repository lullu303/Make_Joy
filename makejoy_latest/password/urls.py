from django.urls import path
from django.contrib.auth import views as auth_views

appname='password'

urlpatterns = [
    path('password_reset/', auth_views.PasswordResetView.as_view(), name="password_reset"),
    path('', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]