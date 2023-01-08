from django.urls import path
from mainapp import views
urlpatterns = [
    path('',views.Home,name="Home")
]
