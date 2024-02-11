from django.urls import path
from . import views 

urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login_user,name='login'),
    path('index',views.index,name='index'),
    path('logout',views.logout_user,name='logout')
]

