from django.urls import path, include
from . import views
urlpatterns = [
path("",views.index,name="index"),
path("pickcar",views.pickcar,name="pickcar"),
#path("details",views.details,name="details")
path('dealdone',views.dealdone,name="dealdone"),
    path('home',views.home,name="home"),
]