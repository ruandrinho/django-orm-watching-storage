from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    non_closed_visits = Visit.objects.filter(leaved_at__isnull=True)
    serialized_visits = []
    for visit in non_closed_visits:
        visit.get_duration()
        serialized_visits.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': localtime(visit.entered_at),
            'duration': visit.format_duration(),
            'is_strange': 'Да' if visit.is_visit_long(60) else ''
        })
    context = {
        'non_closed_visits': serialized_visits,
    }
    return render(request, 'storage_information.html', context)
