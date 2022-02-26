from django.http import Http404, HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render

from tours.service import create_context_main, filter_tours_by_departure,\
    create_context_selected_tour


def main_view(request):
    """открывает главную страницу с 6-ю случайными турами"""
    return render(
        request,
        'tours/index.html',
        context=create_context_main()
        )


def departure_view(request, departure):
    """открывает страницу туров по направлению с выводом всех туров
    этого направления и статистикой о количестве найденых туров, мin/мах цене и
    мin/max колчестве ночей"""
    context = filter_tours_by_departure(departure)
    if context:
        return render(
            request,
            'tours/departure.html',
            context=context)
    else:
        raise Http404


def tour_view(request, id):
    """открывает страницу конкретного тура"""
    context = create_context_selected_tour(id)
    if context:
        return render(
            request,
            'tours/tour.html',
            context=context
        )
    else:
        raise Http404


def custom_handler404(request, exception):
    return HttpResponseNotFound('Страница не найдена')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера')
