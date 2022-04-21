from django.urls import path, include
from . import views
urlpatterns = [
path("",views.index,name="index"),
path("savedata",views.savedata,name="savedata"),
path("check",views.check,name="check"),
path("savedata",views.savedata,name="savedata"),
path("carcheck",views.carcheck,name="carcheck"),



]