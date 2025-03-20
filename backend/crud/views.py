from django.shortcuts import render, redirect # type: ignore
from .models import Customer

def index(request):
    data = {}
    if request.method == "POST":
        a = request.POST["customer_name"]
        b = request.POST["customer_email"]
        c = request.POST["customer_city"]
        obj = Customer(name=a, email=b, city=c)
        obj.save()
    data["record"] = Customer.objects.all()
    return render(request, "index.html", data)

def customer_edit(request, id):
    data = {}
    if request.method == 'POST':
        a = request.POST["customer_name"]
        b = request.POST["customer_email"]
        c = request.POST["customer_city"]
        obj = Customer.objects.get(idCliente=id)
        obj.name = a
        obj.email = b
        obj.city = c
        obj.save()
        return redirect("index")
    data["record"] = Customer.objects.get(idCliente=id)
    return render(request, "customer_edit.html", data)

def customer_delete(request, id):
    Customer.objects.get(idCliente=id).delete()
    return redirect("index")