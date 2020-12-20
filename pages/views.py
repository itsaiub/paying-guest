from django.shortcuts import render
from couches import models, choices
# Create your views here.


def index(request):
    couches = models.Couch.objects.order_by(
        '-list_date').filter(is_published=True)[:3]
    context = {
        'couches': couches,
        'price_choices': choices.price_choices,
        'bedroom_choices': choices.bedroom_choices,
        'division_choices': choices.division_choices,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    realtors = models.Realtor.objects.order_by('-hire_date')

    mvp_realtors = models.Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html', context)
