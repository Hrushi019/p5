from django.urls import path
from appss import views
app_name = "appss"    # is used to create a namespace\\

urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.home,name="home"),
    path('fact/<n>',views.facto,name="facto"),
    #path('secondary suffix',address of function, name of mapping)
]