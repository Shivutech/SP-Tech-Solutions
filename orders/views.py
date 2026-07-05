from django.shortcuts import render, redirect
from .forms import OrderForm


def create_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = OrderForm()

    return render(request, "components/contact.html", {
        "form": form
    })