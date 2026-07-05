from django.shortcuts import render
from orders.forms import OrderForm
from portfolio.models import Portfolio
from services.models import Service

def home(request):
    form = OrderForm()

    portfolios = Portfolio.objects.all().order_by('-created_at')
    services = Service.objects.filter(is_active=True)


    context = {
        'form': form,
        'portfolios': portfolios,
        'services' : services,
    }

    return render(request, 'home.html', context)