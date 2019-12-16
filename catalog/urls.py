from django.urls import path
from . import views


urlpatterns = [
    # Login pages
    path('createaccount', views.createaccount, name='createaccount'),
    path('login', views.login, name='login'),
    # Homepage - search new spots
    path('', views.landingadd, name='home'),
    # Save spot review/wishlist
    path('adddetail/<name>/<lat>/<lng>', views.adddetail, name='adddetail'),
    # Browse spots
    path('browsespots', views.browsespots, name='browsespots'),
    # Find spots
    path('findspots', views.findspot, name='findspot'),

    # Other
    path('landingadd', views.home, name='landingadd'),
    path('userpage', views.userspotlist, name='userspotlist'),
    path('detail/<str:pk>', views.userspotdetail, name='userspotdetail'),
    path('activitystream', views.activitystream, name='activitystream'),
    path('discovernew', views.discovernew, name='discovernew'),
    path('user/<str:pk>', views.userdetail, name='userdetail'),
    path('testpage', views.testpage, name='testpage'),
    path('spotfulldetail/<name>/<city>', views.spotfulldetail, name='spotfulldetail'),
    # path('testpage/<name>/<lat>/<lng>', views.testpagedetail, name='testpagedetail'),
    path('drinking', views.drinkoverview, name='drinkoverview'),
    path('drinkentry/<day>', views.drinkentry, name='drinkentry')
]


# path('testpage', views.testpage, name='testpage'),
# path('testpage/<name>/<lat>/<lng>', views.testpagedetail, name='testpagedetail')
