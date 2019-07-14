from django.urls import path
from . import views


urlpatterns = [
    path('createaccount', views.createaccount, name='createaccount'),
    path('login', views.login, name='login'),
    path('landingadd', views.landingadd, name='landingadd'),
    path('adddetail/<name>/<lat>/<lng>', views.adddetail, name='adddetail'),
    path('findspots', views.findspot, name='findspot'),
    path('', views.home, name='home'),
    path('userpage', views.userspotlist, name='userspotlist'),
    path('detail/<str:pk>', views.userspotdetail, name='userspotdetail'),
    path('activitystream', views.activitystream, name='activitystream'),
    path('discovernew', views.discovernew, name='discovernew'),
    path('user/<str:pk>', views.userdetail, name='userdetail'),
    path('testpage', views.testpage, name='testpage'),
    path('testpage/<name>/<lat>/<lng>', views.testpagedetail, name='testpagedetail')
]


# path('testpage', views.testpage, name='testpage'),
# path('testpage/<name>/<lat>/<lng>', views.testpagedetail, name='testpagedetail')
