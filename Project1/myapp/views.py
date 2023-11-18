from django.shortcuts import render
from .models import Person

# Create your views here.



def welcome(request):
    result = None

    if request.method == "POST":
        mynum = str(request.POST["text"])
        result = mynum 
 
        myinstance = Person(userinputvalue=mynum, mycalcvalue=result)
        myinstance.save()

    return render(request, "index.html", {"result": result})


def about_fun(request):
    return render(request, "about.html")


def contactus_fun(request):
    return render(request, "contactus.html")


def login_fun(request):
    return render(request, "loginform.html")
