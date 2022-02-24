from random import sample

from django.http import Http404, HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render

import tours.data as data


def main_view(request):
    title = data.title
    subtile = data.subtitle
    description = data.description
    random_tours = dict(sample(data.tours.items(), 6))

    return render(
        request,
        'tours/index.html',
        context={
            "title": title,
            "subtile": subtile,
            "description": description,
            "tours": random_tours,
            }
        )


def departure_view(request, departure):
    tours = data.tours
    flying_from = data.departures.get(departure)
    filter_tours = {}
    data_tours = {
        'count_tours': 0,
        'max_price': 0,
        'max_nights': 0
    }
    for id in tours.keys():
        if tours.get(id).get('departure') == departure:
            filter_tours[id] = tours.get(id)
            data_tours['count_tours'] += 1

            if data_tours.get('max_price') < tours.get(id).get('price'):
                data_tours['max_price'] = tours.get(id).get('price')

            if not data_tours.get('min_price') or data_tours.get('min_price') > tours.get(id).get('price'):
                data_tours['min_price'] = tours.get(id).get('price')

            if data_tours.get('max_nights') < tours.get(id).get('nights'):
                data_tours['max_nights'] = tours.get(id).get('nights')

            if not data_tours.get('min_nights') or data_tours.get('min_nights') > tours.get(id).get('nights'):
                data_tours['min_nights'] = tours.get(id).get('nights')

    if filter_tours:
        return render(
            request,
            'tours/departure.html',
            context={
                'filter_tours': filter_tours,
                'flying_from': flying_from,
                'data_tors': data_tours
                }
            )
    else:
        raise Http404


def tour_view(request, id):
    tour = data.tours.get(id)
    if tour:
        flying_from = data.departures.get(tour['departure'])
        return render(
            request,
            'tours/tour.html',
            context={
                'tour': tour,
                'flying_from': flying_from
            }
        )
    else:
        raise Http404


def custom_handler404(request, exception):
    return HttpResponseNotFound('Страница не найдена')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера')
