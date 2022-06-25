from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    this_passcard_visits = Visit.objects.filter(passcard=passcard)
    serialized_visits = []
    for visit in this_passcard_visits:
        visit.get_duration()
        serialized_visits.append({
            'is_strange': 'Да' if visit.is_visit_long() else '',
            'duration': visit.format_duration(),
            'entered_at': localtime(visit.entered_at)
        })
    context = {
        'passcard': passcard,
        'this_passcard_visits': serialized_visits
    }
    return render(request, 'passcard_info.html', context)
