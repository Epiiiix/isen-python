from django.shortcuts import redirect
from django.views.generic import ListView
from products.models import Product

def RedirectHomeView(request):
    '''
    Redirect url from '/' to '/home/'
    '''
    return redirect('home')

class HomeView(ListView):
    '''
    Renders home page with all the products
    '''
    template_name = 'home.html'
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        min_price = self.request.GET.get("min_price")
        max_price = self.request.GET.get("max_price")
        sort = self.request.GET.get("sort")

        if min_price and not min_price.isnumeric():
            min_price = None  # If not numeric, ignore it
        if max_price and not max_price.isnumeric():
            max_price = None  # If not numeric, ignore it

        if min_price:
            queryset = queryset.filter(price__gte=int(min_price))
        if max_price:
            queryset = queryset.filter(price__lte=int(max_price))

        if sort == "asc":
            queryset = queryset.order_by("price")
        elif sort == "desc":
            queryset = queryset.order_by("-price")
        else:
            queryset = queryset.order_by("price")

        return queryset
