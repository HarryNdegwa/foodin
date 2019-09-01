from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string

from .forms import ReserveForm, ContactForm, CommentForm
from .models import Meal


def home(request):
    meals = Meal.objects.all()[:6]
    r_form = ReserveForm()
    c_form = ContactForm()
    com_form = CommentForm()
    return render(
        request,
        "index.html",
        {"r_form": r_form, "c_form": c_form, "com_form": com_form, "meals": meals},
    )


def get_meals(request):
    meal_type = request.GET.get("type")
    if meal_type == "all":
        meals = Meal.objects.all()
    else:
        meals = Meal.objects.filter(category__name=meal_type)
    meal_html = render_to_string(meal_type + ".html", {"meals": meals})

    data = {"meal_html": meal_html}

    return JsonResponse(data)
