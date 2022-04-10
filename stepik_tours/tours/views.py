from django.shortcuts import render

departures = {"msk": "из Москвы", "spb": "из Петербурга", "nsk": "из Новосибирска", "ekb": "из Екатеринбурга",
              "kazan": "из Казани"}


def main_view(request):
    return render(request, 'tours/index.html')


def departure_view(request, departure):
    departure = departures.get(departure)
    return render(request, 'tours/departure.html', {'departure': departure})


def tour_view(request, id):
    return render(request, 'tours/tour.html')
