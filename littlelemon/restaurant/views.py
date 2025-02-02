from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

# Create your views here.
# def index(request):
#    return render(request, 'index.html', {})

def index(request):
    return render(request, 'index.html')

# Handles GET (list all items) and POST (create new item)
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# Handles GET (retrieve single item), PUT (update item), and DELETE (remove item)
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    # Specify the model for the viewset
    queryset = Booking.objects.all()  # Fetch all booking objects
    serializer_class = BookingSerializer  
