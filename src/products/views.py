from django.views.generic import ListView
from .models import Product

class HomePageView(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'products'
