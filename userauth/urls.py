from django.urls import path

from userauth import views

app_name = 'userauth'

urlpatterns = [
    path('sing-up/', views.register_view, name='sing-up'),
    path('sing-in/', views.login_view, name='sing-in'),
    path('sing-out/', views.logout_view, name='sing-out')
]
