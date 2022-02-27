from random import sample

import tours.data as data


def create_context_main():
    """формирует контекст для главной старницы"""
    context = {
        'title': data.title,
        'subtile': data.subtitle,
        'description': data.description,
        'tours': dict(sample(data.tours.items(), 6))
    }
    return context


def filter_tours_by_departure(departure):
    """формирует контекст для сранички туров по направлению. Если по departure
    ничего не найдено, возвращает None"""
    tours = data.tours
    flying_from = data.departures.get(departure)
    filter_tours = {}
    count_tours = 0
    for id in tours.keys():
        if tours.get(id).get('departure') == departure:
            filter_tours[id] = tours.get(id)
            count_tours += 1

    if filter_tours:
        data_tours = {
        'count_tours': count_tours,
        'max_price': max(filter_tours.get(id).get('price') for id in filter_tours),
        'max_nights': max(filter_tours.get(id).get('nights') for id in filter_tours),
        'min_price': min(filter_tours.get(id).get('price') for id in filter_tours),
        'min_nights': min(filter_tours.get(id).get('nights') for id in filter_tours),
        }
        return {
            'filter_tours': filter_tours,
            'flying_from': flying_from,
            'data_tors': data_tours
            }
    else:
        return None


def create_context_selected_tour(id):
    tour = data.tours.get(id)
    if tour:
        flying_from = data.departures.get(tour['departure'])
        return {
            'tour': tour,
            'flying_from': flying_from
            }
    else:
        return None
