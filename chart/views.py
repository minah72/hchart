from django.shortcuts import render
from .models import Passenger
from django.db.models import Count, Q

def home(request):
    return render(request, 'home.html')

def world_population(request):
    return render(request, 'world_population.html')

def ticket_class_view_1(request):  # 방법 1
    dataset = Passenger.objects \
        .values('ticket_class') \
        .annotate(
            survived_count=Count('ticket_class',
                                 filter=Q(survived=True)),
            not_survived_count=Count('ticket_class',
                                     filter=Q(survived=False))) \
        .order_by('ticket_class')
    return render(request, 'ticket_class_1.html', {'dataset': dataset})
#  dataset = [
#    {'ticket_class': 1, 'survived_count': 200, 'not_survived_count': 123},
#    {'ticket_class': 2, 'survived_count': 119, 'not_survived_count': 158},
#    {'ticket_class': 3, 'survived_count': 181, 'not_survived_count': 528}
#  ]

def ticket_class_view_2(request):  # 방법 2
    pass

def ticket_class_view_3(request):  # 방법 3
    pass

def json_example(request):  # 방법 4
    pass

def chart_data(request):  # 방법 4
    pass