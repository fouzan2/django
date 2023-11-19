from django.shortcuts import render
from .models import Person
from openai import OpenAI

client = OpenAI(api_key="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")


# Create your views here.
def gpt_process(string_value):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": string_value},
            {"role": "system", "content": "You are a helpful assistant."},
        ],
    )
    return str(completion.choices[0].message.content)


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


def about_fun(request):
    return render(request, "about.html")


def contactus_fun(request):
    return render(request, "contactus.html")


def login_fun(request):
    return render(request, "loginform.html")
