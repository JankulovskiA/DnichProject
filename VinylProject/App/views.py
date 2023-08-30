from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def catalog(request):
    return render(request, "catalog.html")

def order(request):
    return render(request, "order.html")

def payment(request):
    return render(request, "payment.html")

def cart(request):
    return render(request, "cart.html")

def success(request):
    return render(request, "success.html")

def sell(request):
    return render(request, "sell.html")

def submitted(request):
    return render(request, "submitted.html")

