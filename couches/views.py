from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from . import models, choices

# Create your views here.


def index(request):
    couches = models.Couch.objects.order_by(
        '-list_date').filter(is_published=True)

    paginator = Paginator(couches, 6)
    page = request.GET.get('page')
    paged_couches = paginator.get_page(page)

    context = {
        'couches': paged_couches
    }
    return render(request, 'couches/couches.html', context)


def couch(request, couch_id):
    couch = get_object_or_404(models.Couch, pk=couch_id)

    context = {
        'couch': couch
    }

    return render(request, 'couches/couch.html', context)


def search(request):

    queryset_list = models.Couch.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(
                city__iexact=city)

    # division
    if 'division' in request.GET:
        division = request.GET['division']
        if division:
            queryset_list = queryset_list.filter(
                division__iexact=division)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(
                bedrooms__lte=bedrooms)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(
                price__lte=price)

    paginator = Paginator(queryset_list, 3)
    page = request.GET.get('page')
    paged_spots = paginator.get_page(page)

    context = {
        'price_choices': choices.price_choices,
        'bedroom_choices': choices.bedroom_choices,
        'division_choices': choices.division_choices,
        'spots': paged_spots,
        'values': request.GET
    }

    return render(request, 'couches/search.html', context)
