from django.shortcuts import render
from orders.forms import OrderForm
from portfolio.models import Portfolio
from services.models import Service
from testimonials.models import Testimonial
from faq.models import FAQ

def home(request):
    form = OrderForm()

    portfolios = Portfolio.objects.all().order_by('-created_at')
    services = Service.objects.filter(is_active=True)
    testimonials = Testimonial.objects.all().order_by("-created_at")
    faqs = FAQ.objects.all()



    context = {
        'form': form,
        'portfolios': portfolios,
        'services' : services,
         'testimonials': testimonials,
         'faqs' : faqs,
    }

    return render(request, 'home.html', context)

from django.shortcuts import render
from orders.models import Order
from services.models import Service
from portfolio.models import Portfolio

def dashboard(request):
    context = {
        "total_orders": Order.objects.count(),
        "total_services": Service.objects.count(),
        "total_projects": Portfolio.objects.count(),
        "recent_orders": Order.objects.order_by("-created_at")[:5],
    }
    return render(request, "dashboard.html", context)