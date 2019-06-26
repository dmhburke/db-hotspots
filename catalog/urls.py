from django.urls import path
from . import views


urlpatterns = [
    path('createaccount', views.createaccount, name='createaccount'),
    path('login', views.login, name='login'),
    path('', views.home, name='home'),
    path('userpage', views.userspotlist, name='userspotlist'),
    path('detail/<str:pk>', views.userspotdetail, name='userspotdetail'),
    path('activitystream', views.activitystream, name='activitystream'),
    path('discovernew', views.discovernew, name='discovernew'),
    path('user/<str:pk>', views.userdetail, name='userdetail'),
    path('testpage', views.testpage, name="testpage"),
]
