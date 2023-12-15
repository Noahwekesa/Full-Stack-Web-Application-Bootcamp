from django.views.generic import DetailView, ListView
from .models import Product

class HomePageView(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all().order_by('-id')[:4]

class ProductDetailView(DetailView):
    model = Product
