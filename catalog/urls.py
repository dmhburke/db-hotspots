from django.urls import path
from . import views


urlpatterns = [
    path('createaccount', views.createaccount, name='createaccount'),
    path('login', views.login, name='login'),
    path('', views.landingadd, name='home'),
    path('adddetail/<name>/<lat>/<lng>', views.adddetail, name='adddetail'),
    path('findspots', views.findspot, name='findspot'),
    path('landingadd', views.home, name='landingadd'),
    path('browsespots', views.browsespots, name='browsespots'),
    path('userpage', views.userspotlist, name='userspotlist'),
    path('detail/<str:pk>', views.userspotdetail, name='userspotdetail'),
    path('activitystream', views.activitystream, name='activitystream'),
    path('discovernew', views.discovernew, name='discovernew'),
    path('user/<str:pk>', views.userdetail, name='userdetail'),
    path('testpage', views.testpage, name='testpage'),
    path('spotfulldetail/<name>/<city>', views.spotfulldetail, name='spotfulldetail'),
    path('testpage/<name>/<lat>/<lng>', views.testpagedetail, name='testpagedetail'),
    path('drinking', views.drinkoverview, name='drinkoverview'),
    path('drinkentry/<day>', views.drinkentry, name='drinkentry')
]


# path('testpage', views.testpage, name='testpage'),
# path('testpage/<name>/<lat>/<lng>', views.testpagedetail, name='testpagedetail')
