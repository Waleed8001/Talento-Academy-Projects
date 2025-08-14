from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('courses/', views.Allcourse, name='allcourses'),
    path('courses/search/', views.filteredcourse, name='courses'),
    path('webinars/', views.AllWebinars, name='allwebinars'),
    path('contactus/', views.Contact_Us, name='contactus'),
    path('courses/<int:id>/', views.selectedcourse, name='selectedcourse'),
    path('testimonial/', views.AllTestimonial, name='alltestimonial'),    
    path('aboutus/', views.aboutus, name='aboutus'),    
]