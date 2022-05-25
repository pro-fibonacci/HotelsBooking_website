from django.shortcuts import render
from .models import *
from django.http import FileResponse
import io 
import csv
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
# Create your views here.
def about(request):
     context = {}
     return render(request, 'pages/about.html', context)

def pdf(request):
     buffer = io.BytesIO()
     c = canvas.Canvas(buffer, pagesize=letter, bottomup=0)
     textob = c.beginText()
     textob.setTextOrigin(inch, inch)
     textob.setFont("Helvetica", 14)

     lines = []

     for book in booked:
          lines.append(book.departure)
          lines.append(book.arrival)
          lines.append(book.email)
          lines.append(book.rooms)
          lines.append("=========")

     for line in lines:
          textob.textLine(line)

          c.drawText(textob)
          c.showPage()
          c.save()
          buffer.seek(0)

     response = FileResponse(buffer, content_type='Line')
     response['Content-Disposition'] = 'attachment; filename="HotelOrder.pdf"'
     return response


def blog(request):
     context = {}
     return render(request, 'pages/blog.html', context)

def contact(request):
      context = {}
      return render(request, 'pages/contact.html', context)

def bookings(request):
      context = {}
      return render(request, 'pages/bookings.html', context)

def gallery(request):
     context = {}
     return render(request, 'pages/gallery.html', context)

def index(request):
	home_details = home.objects.all()
	context = {"home": home_details}
	return render(request, 'pages/index.html', context)

def room(request):
      context = {}
      return render(request, 'pages/room.html', context)

def submitted_contact(request):
     name = request.POST['name']
     email = request.POST['email']
     phone = request.POST['phone']
     message = request.POST['message']

     details_info = contacting(name=name, email=email, phone=phone, message=message)
     details_info.save()
     return render(request, 'pages/contact.html')


def submitted_bookings(request):
     email = request.POST['email']
     arrival = request.POST['arrival']
     departure = request.POST['departure']
     rooms = request.POST['rooms']

     details_book = booked(email=email, arrival=arrival, departure=departure, rooms=rooms)
     details_book.save()
     return render(request, 'pages/bookings.html')

def base(request):
     context = {}
     return render(request, 'pages/base.html', context)