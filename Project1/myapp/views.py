from django.shortcuts import render, redirect
from .models import Person
from openai import OpenAI

client = OpenAI(api_key="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")

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
def gpt_process(string_value):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": string_value},
        ],
    )
    return str(completion.choices[0].message.content)


@login_required(login_url='login')
def welcome(request):
    result = None

    if request.method == "POST":
        user_input_text = str(request.POST["text"])
        try:
            gpt_output = gpt_process(user_input_text)
            result = gpt_output
            myinstance = Person(userinputvalue=user_input_text, mycalcvalue=gpt_output)
            myinstance.save()
        except:
            result = "Something went wrong. Please try again!"

    return render(request, "index.html", {"result": result})


@login_required
def about_fun(request):
    return render(request, "about.html")


@login_required
def contactus_fun(request):
    return render(request, "contactus.html")


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("welcome")
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


def logoutUser(request):
    logout(request)
    return redirect("login")
