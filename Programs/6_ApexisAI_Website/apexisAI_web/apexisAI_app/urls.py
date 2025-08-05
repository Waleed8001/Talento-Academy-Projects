from django.urls import path
from .views import MyPlatform, MyAboutus, MyContactus


urlpatterns = [
    path('platform/', MyPlatform, name="home"),
    path('platform/', MyPlatform, name="platform"),
    path('aboutus/', MyAboutus, name="aboutus"),
    path('contactus/', MyContactus, name="contactus"),
]

