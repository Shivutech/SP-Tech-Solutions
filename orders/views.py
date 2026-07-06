from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import OrderForm
from django.core.mail import send_mail
from django.conf import settings 


def create_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid(): 
            order = form.save()

            send_mail(
               subject=f"New Order Received - {order.service}",
               message=f"""
        New Service Order

        Name: {order.name}
        Email: {order.email}
        Phone: {order.phone}

        Service: {order.service}
        Budget: {order.budget}

        Message:
        {order.message}
       """,
    from_email=settings.EMAIL_HOST_USER,
    recipient_list=[settings.EMAIL_HOST_USER],
    fail_silently=False,
)
            messages.success(
                request,
                "✅ Thank you! Your request has been submitted successfully. We will contact you soon."
            )
            return redirect("/#contact")
    else:
        form = OrderForm()

    return render(request, "components/contact.html", {"form": form})