import tours.data as data


def base_departure(request):
    departures = data.departures
    return {'departures': departures}
