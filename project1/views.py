from django.shortcuts import render

from app.models import Product




def abc(request):
    data=Product.object.all()
    context={"data":data}
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
