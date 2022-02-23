from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseServerError
import random as rd

import tours.data as data


def main_view(request):
    title = data.title
    subtile = data.subtitle
    description = data.description
    departures = data.departures
    tours = {}
    dropped_ids = []

    while True:
        id = rd.randint(1, len(data.tours.keys()))

        if id not in dropped_ids:
            dropped_ids.append(id)
            tours[id] = data.tours.get(id)

        if len(dropped_ids) == 6:
            break

    return render(
        request,
        'tours/index.html',
        context={
            "title": title,
            "subtile": subtile,
            "description": description,
            "tours": tours,
            'departures': departures
            }
        )


def departure_view(request, departure):
    tours = data.tours
    departures = data.departures
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

    return render(
        request,
        'tours/departure.html',
        context={
            'filter_tours': filter_tours,
            'departure': data.departures.get(departure),
            'data_tors': data_tours,
            'departures': departures
            }
        )


def tour_view(request, id):
    tour = data.tours.get(id)
    departures = data.departures
    if tour:
        departure = data.departures.get(tour['departure'])
        return render(
            request,
            'tours/tour.html',
            context={
                'tour': tour,
                'dep': departure,
                'departures': departures
            }
        )
    else:
        raise Http404


def custom_handler404(request, exception):
    return HttpResponseNotFound('Страница не найдена')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера')
