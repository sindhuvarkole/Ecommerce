from django.shortcuts import redirect, render

from app.models import Product


# Create your views here.
def index(request):
    data=Product.objects.all()
    context={"data":data}
    return render(request,"index.html",context)
def about(request):
    return render(request,"about.html")
def insertdata(request):
    if request.method=="POST":
        name=request.POST.get('name')
        id=request.POST.get('id')
        price=request.POST.get('price')
        query=Product(name=name,id=id,price=price)
        query.save()
        return render(request,"index.html")
def UpdateData(request,id):
    d=Product.objects.get(id=id)
    context={"d":d}

    if request.method=="POST":
       name=request.POST.get('name')
       id=request.POST.get('id')
       price=request.POST.get('price')

       edit=Product.objects.get(id=id)
       edit.name=name
       edit.id=id
       edit.price=price

       query=Product(name=name,id=id,price=price)
       query.save()
       return redirect("/")
    return render(request,"edit.html",context)
def deleteData(request,id):
    d=Product.objects.get(id=id)
    d.delete()
    return redirect("/")

        

