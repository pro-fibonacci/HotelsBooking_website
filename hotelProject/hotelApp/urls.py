
from django.urls import path

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.index, name="index"),
	path('about/', views.about, name="about"),
	path('contact/', views.contact, name="contact"),
	path('pdf/', views.pdf, name="pdf"),
	path('submitted_contact/', views.submitted_contact, name="submitted_contact"),
	path('submitted_bookings/', views.submitted_bookings, name="submitted_bookings"),
	path('gallery/', views.gallery, name="gallery"),
	path('blog/', views.blog, name="blog") ,
	path('bookings/', views.bookings, name="bookings"),
	path('room/', views.room, name="room"),

]