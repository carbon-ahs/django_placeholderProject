from django.shortcuts import render


# Create your views here.
def home(request):
    context = {
        "test": "TEST",
    }
    return render(request, "core/home.html", context=context)


def something_cool(request):
    context = {
        "test": "something_cool",
    }
    return render(request, "core/something_cool.html", context=context)
